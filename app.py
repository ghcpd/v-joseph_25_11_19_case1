from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
archived_tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, archived_tasks=archived_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    color = request.form.get('color', 'white')
    tasks.append({'title': title, 'color': color})
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))

@app.route('/archive/<int:index>')
def archive_task(index):
    if 0 <= index < len(tasks):
        archived_tasks.append(tasks.pop(index))
    return redirect(url_for('index'))

@app.route('/update_color/<int:index>', methods=['POST'])
def update_color(index):
    if 0 <= index < len(tasks):
        color = request.form.get('color')
        tasks[index]['color'] = color
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)