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

@app.route('/delete/<int:item_id>', methods=['POST'])
def del_item(item_id):
    item = Item.query.get(item_id)  # Menggunakan item_id yang diterima sebagai parameter
    if item:
        # Hapus item dari database
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect ke halaman utama
    else:
        return "Item not found", 404

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)  # Ambil item berdasarkan ID atau tampilkan 404 jika tidak ditemukan
    if request.method == 'POST':
        # Update item berdasarkan data dari form
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()  # Simpan perubahan ke database
        return redirect(url_for('index'))  # Redirect ke halaman index

    return render_template('edit_item.html', item=item)