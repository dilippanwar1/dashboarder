from flask import Flask, render_template, jsonify
from celery import Celery
import time

app = Flask(__name__, template_folder='Templates')
app.config['CELERY_BROKER_URL'] = 'redis://0.0.0.0:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://0.0.0.0:6379'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task/<name>')
def task(name):
    task = run_task.delay(name)
    return jsonify({'taskid':task.id})

@celery.task
def run_task(name):
    time.sleep(30)
    return {'name':name}

@app.route('/poll/<taskid>')
def poll(taskid):
    task = run_task.AsyncResult(taskid)
    data = task.info if task.state == "SUCCESS" else None
    return jsonify({'state': task.state, 'data':data})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, threaded=True)