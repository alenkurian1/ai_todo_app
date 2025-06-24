from flask import Flask, request, render_template, redirect
import random

app = Flask(__name__)
tasks = []

def ai_label(task):
    labels = ['Work', 'Personal', 'Urgent', 'Low Priority']
    return random.choice(labels)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        label = ai_label(content)
        tasks.append({'content': content, 'label': label})
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
