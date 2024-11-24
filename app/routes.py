# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Item

@app.route('/')
def index():
    items = Item.query.all()  # Mengambil semua item dari database
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        
        # Menambahkan item baru ke database
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect ke halaman index

    return render_template('add_item.html')
