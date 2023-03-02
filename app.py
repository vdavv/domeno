from flask import Flask, render_template, request, jsonify
import time
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    with open('data.json', 'r') as openfile:
        # Reading from json file
        data = json.load(openfile)
    # counter = 0
    # website = ''
    # commerce = ''
    message = request.json['message']
    response = {}

    if message == 'init':
        response[
            'message'] = 'Проверьте домен на нарушение товарных знаков. Защитите себя от исков на сумму до 5 миллионов рублей'
        response['sender'] = 'chatbot'
        response[
            'next_message'] = 'Для проверки введите домен до точки (без .ru .com .org). Пример: вместо cola.cola.ru, введите cola.cola'
        response['next_sender'] = 'chatbot'

    else:
        if 'shutdown' in data.keys():
            if data['shutdown']:
                quit()

        if data['counter'] == 0:
            data['website'] = message
            time.sleep(1)
            response['message'] = "Вы используете сайт для продажи товаров (оказания услуг)?"
            response['sender'] = 'chatbot'

        elif data['counter'] == 1:
            data['commerce'] = message
            time.sleep(1)
            if message.lower() == "нет":
                response[
                    'message'] = "Некоммерческое использование товарного знака в домене является законным, однако не исключает возможных претензий со стороны правообладателя. Консультация со специалистом поможет их избежать, обращайтесь к ___*гиперссылка на юр. сервис*"
                response['sender'] = 'chatbot'
                response['next_message'] = 'Хотите продолжить проверку?'
                response['next_sender'] = 'chatbot'
                data.update({'continue_check': ''})

            elif message.lower() == 'да':
                response['message'] = 'Выберите категорию(-ии) товаров или услуг из списка'
                response['sender'] = 'chatbot'
                data.update({'category': '', 'category_handle': 1})

        elif 'continue_check' in data.keys():
            data['continue_check'] = message
            if message.lower() in ["да"]:
                data.pop('continue_check')
                response['message'] = data
                response['sender'] = 'chatbot'
                # further code here

            elif message.lower() in ['нет']:
                response['message'] = 'Хорошо, спасибо за уделённое время!'
                response['sender'] = 'chatbot'
                data.update({'shutdown': 1})

        data['counter'] += 1
        write_to_json(data)

    return jsonify(response)


if __name__ == '__main__':
    def write_to_json(data):
        with open("data.json", "w", encoding='utf8 ') as json_file:
            json_file.write(json.dumps(data, ensure_ascii=False))


    write_to_json({"counter": 0, "website": '', "commerce": ''})
    app.run(debug=True)
