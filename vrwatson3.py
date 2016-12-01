# Visual Recognition with IBM Watson - Facial Recognition
# Requirements 1: IBM Bluemix Account (free) - https://console.ng.bluemix.net/
# Requirements 2: watson_developer_cloud module python module
# Once registered, login to your account, go to Services -> Watson and create a Visual Recognition instance
# Once you have your VR instance created, you will use its API credentials in your python code

from watson_developer_cloud import VisualRecognitionV3 as vr

# creating a VR instance

instance = vr(api_key='paste your api _key here', version='2016-05-20')

# select an image (local or url) with people in it. Detecting faces:

img = instance.detect_faces(images_url='url-path-to-img.jpg')

# you can run this code in the interpreter. If you request >>> img it will output a json formatted result
# if your image contains public and well known people, Watson can confidently recogize them:

for identity in img['images'][0]['faces']:
    print(identity['identity']['name'], identity['gender'])
    
# I posted a demo of this here: http://bit.ly/2gcWiPZ
# If you need help with Watson and Visual Recognition, send me a message. 
