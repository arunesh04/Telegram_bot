from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "5598309398:AAE-6HBjxk_Urpavf1NtY4tCF_p-Yr320VQ"
 
app = Flask(__name__)
 
def parse_message(message):
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
 
        return chat_id,txt
    except:
        print("NO text found")
 
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
 
    return r  
def send_courseudemy(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "The listed course are from",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Udemy",
                    "callback_data": "ic_A"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r
def send_courseera(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "The listed course type is from",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Coursera",
                    "callback_data": "ic_A"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r
def send_website(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Type the website below to search for the course",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "UDEMY",
                    "callback_data": "ic_A"
                },
                {
                    "text": "COURSERA",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r
def send_coursename2(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Type the required course given below loaded in our server   ",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "WEB DEVELOPMENT",
                    "callback_data": "ic_Z"
                },
                {
                    "text": "PROGRAMMING LANGUAGES",
                    "callback_data": "ic_W"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r
def send_coursename1(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Type the required course given below loaded in our server   ",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "MACHINE LEARNING",
                    "callback_data": "ic_X"
                },
                {
                    "text": "FLUTTER",
                    "callback_data": "ic_Y"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r
@ app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        
        try:
            chat_id, txt = parse_message(msg)
            txt=txt.lower()
            if txt == "hii":
                send_message(chat_id,"Hello,Troubled in searching the top courses!!\nNo Worries when Course bot is here")
                send_website(chat_id)
            elif txt == "udemy":
                send_coursename1(chat_id)
            elif txt == "machine learning":
                send_courseudemy(chat_id)
                send_message(chat_id,"https://www.udemy.com/course/machinelearning/")
                send_message(chat_id, "https://www.udemy.com/course/complete-machine-learning-and-data-science-zero-to-mastery/")
                send_message(chat_id, "https://www.udemy.com/course/data-science-and-machine-learning-with-python-hands-on/")
                send_message(chat_id, "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/")
                send_message(chat_id,"https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/")
            elif txt == "flutter":
                send_courseudemy(chat_id)
                send_message(chat_id,"https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/")
                send_message(chat_id, "https://www.udemy.com/course/flutter-bootcamp-with-dart/")  
                send_message(chat_id, "https://www.udemy.com/course/flutter-firebase-2022-complete-bundle-build-3-apps/")
                send_message(chat_id,"https://www.udemy.com/course/flutter-advanced-course-clean-architecture-with-mvvm/")
                send_message(chat_id,"")
            elif txt=="course era":
                send_coursename2(chat_id)
            elif txt=="web development":
                send_courseera(chat_id)
                send_message(chat_id,"https://in.coursera.org/learn/html-css-javascript-for-web-developers")
                send_message(chat_id,"https://in.coursera.org/professional-certificates/meta-front-end-developer")
                send_message(chat_id,"https://in.coursera.org/professional-certificates/ibm-full-stack-cloud-developer")
            elif txt == "programming languages":
                send_courseera(chat_id)
                send_message(chat_id,"https://in.coursera.org/specializations/python")
                send_message(chat_id, "https://in.coursera.org/learn/programming-languages")
                send_message(chat_id, "https://in.coursera.org/specializations/coding-for-everyone")
            else:
                send_message(chat_id, 'Sorry we could not recogonise your message,Please continue with Hii')
        except:
            print("Index")
 
        return Response('ok', status=200)
    else:
        return "<h1>HII</h1>"
 
if __name__ == '__main__':
    app.run(threaded=True,debug=True)