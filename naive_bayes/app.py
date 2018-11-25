from flask import Flask, render_template, jsonify, request
from SentimentClassification import SentimentClassification

tcp = SentimentClassification()
tcp.get_train_data("aaa")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    sentence = request.form['text']
    tcp = SentimentClassification()
    predic = tcp.get_train_data(sentence)

    dict = []
    dict.append(predic)
    dict.append(sentence)

    return render_template('index.html', dict=dict)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
