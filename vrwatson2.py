# Visual Recognition with IBM Watson - Text Recognition
# Requirements 1: IBM Bluemix Account (free) - https://console.ng.bluemix.net/
# Requirements 2: watson_developer_cloud module python module
# Once registered, login to your account, go to Services -> Watson and create a Visual Recognition instance
# Once you have your VR instance created, you will use its API credentials in your python code

from watson_developer_cloud import VisualRecognitionV3 as vr

# creating a VR instance

instance = vr(api_key='paste your api _key here', version='2016-05-20')

# select an image (local or url) with text in it. Recognizing text:

img = instance.recognize_text(images_url='url-path-to-img.jpg')

# you can run this code in the interpreter. If you request >>> img it will output a json formatted result
# going down the json tree, you can retrieve the text in the image with the following command:

print(img['images'][0]['text'])

    
# I posted a demo of this here: http://bit.ly/2hlC20a
# If you need help with Watson and Visual Recognition, send me a message. 
