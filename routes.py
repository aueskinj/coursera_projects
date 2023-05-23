from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime

import forms

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to the database')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

#passes info to the route functions, edit has function to task id
@app.route('/edit/<int:task_id>')
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    print(task)
    if task:
        form.title.data = task.title
        return render_template('edit.html', form=form)
    return redirect(url_for('index'))