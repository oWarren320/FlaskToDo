from flask import render_template, request, redirect, url_for, abort
from app import app
from app.models import Todo
from app import db

@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    todo = Todo.query.get_or_404(id)
    todo.complete = True
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.get(int(id))
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get_or_404(id)

    if request.method == 'POST':
        new_text = request.form['todoitem']
        todo.text = new_text
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo)
