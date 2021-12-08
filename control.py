import os
from flask import Flask, render_template, request, redirect, flash
from mydb import mydb, mycursor
from werkzeug.utils import secure_filename

import string
import random

username= "theoDc"
password="ozumba mbadiwe"
size=1500
randomlink = ''.join(random.choices(string.ascii_letters+string.digits, k= size))  
randomStrings= str(randomlink)


app = Flask(__name__)

LINKERS='static/blgImg'
app = Flask(__name__)
app.config['UPLOAD FOLDER']= LINKERS

@app.route('/')
def home():
    rand=randomStrings
    mycursor.execute("SELECT * FROM admins")
    lists= mycursor.fetchall()
    return render_template('index.html' , lists=lists, rand=rand)

@app.route(f'/{randomStrings}/admin', methods=['GET', 'POST'])
def admin():
    rand=randomStrings
    mycursor.execute('SELECT * FROM admins')
    all= mycursor.fetchall()
    if request.method== 'POST':
        _title= request.form['Title']
        _desc = request.form['Descriptions']
        f = request.files['IMG']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD FOLDER'], filename))

        mycursor.execute(f'INSERT INTO admins(Title, Descriptions, IMG) VALUES("{_title}", "{_desc}", "{filename}")')
        mydb.commit()
        return redirect('/')
    return render_template("admin.html", rand=rand, all=all)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    rand=randomStrings
    msg=''
    if request.method == 'POST':
        usern= request.form['username']
        passw= request.form['pass']
        if usern==username and passw== password:
            return redirect(f'/{rand}/admin')
        else:
            msg='wrong Input'

    return render_template('adminlogin.html', rand=rand, msg=msg)

@app.route('/home/<int:id>')
def bloger(id):
    mycursor.execute(f'SELECT * FROM admins WHERE ID={id}')
    news= mycursor.fetchone()
    return render_template('bloger.html', news=news)

@app.route(f'/delete/{randomStrings}/<int:id>')
def delete(id):
    mycursor.execute(f'DELETE FROM admins WHERE id={id}')
    return redirect(f'/{randomStrings}/admin')
if __name__ == '__main__':
    app.run(debug=True)