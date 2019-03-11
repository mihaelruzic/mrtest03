from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Openshift Jenkins Pipeline Python/Nginx Implementation',
        'description': 'Find the implementation at https://github.com/ruddra/openshift-python-nginx'
    },
    {
        'id': 2,
        'title': 'Openshift Jenkins Pipeline Django Implementation',
        'description': 'Find the implementation at https://github.com/ruddra/openshift-django'
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    #return jsonify({'tasks': tasks})
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='localhost')