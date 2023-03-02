from flask import Flask, request, jsonify
import time

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message']
    response = {}

    if message == 'init':
        if 'init_count' not in request.cookies:
            response['message'] = 'Hi there! How can I help you today?'
            response['sender'] = 'chatbot'
            response['next_message'] = 'Do you have any specific questions or concerns?'
            response['next_sender'] = 'chatbot'
            response['init_count'] = 1
        elif int(request.cookies['init_count']) == 1:
            response['message'] = 'Welcome back! How can I assist you?'
            response['sender'] = 'chatbot'
            response['next_message'] = 'Do you have any new questions or concerns?'
            response['next_sender'] = 'chatbot'
            response['init_count'] = 2
        else:
            response['message'] = 'Welcome back again! How can I help you?'
            response['sender'] = 'chatbot'
            response['init_count'] = 3
        response['cookie'] = 'init_count={}'.format(response['init_count'])
    else:
        # code for processing other messages goes here
        pass

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
