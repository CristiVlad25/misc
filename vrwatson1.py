# Visual Recognition with IBM Watson - Image Classification
# Requirements 1: IBM Bluemix Account (free) - https://console.ng.bluemix.net/
# Requirements 2: watson_developer_cloud module python module
# Once registered, login to your account, go to Services -> Watson and create a Visual Recognition instance
# Once you have your VR instance created, you will use its API credentials in your python code

from watson_developer_cloud import VisualRecognitionV3 as vr

# creating a VR instance

instance = vr(api_key='paste your api _key here', version='2016-05-20')

# select an image (local or url). Copy its location (path or url):

img = instance.classify(images_url='url-path-to-img.jpg')

# you can run this code in the interpreter. If you request >>> img it will output a json formatted result
# getting down the json tree with the following input will display what Watson sees in the image, and the confidence level

# >>> img['images'][0]['classifiers'][0]['classes']

# for a better view of the results, you can use pprint

import pprint
pprint.pprint(img['images'][0]['classifiers'][0]['classes'])
    
# I posted a demo of this here: http://bit.ly/2gZg4D9
# If you need help with Watson and Visual Recognition, send me a message. 
