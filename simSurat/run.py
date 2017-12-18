from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import datetime

conn = MongoClient('127.0.0.1:27017')
db = conn.simSurat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginUser', methods = ['POST', 'GET'])
def loginUser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        temprow = {}
        temprowdataform1 = []
        temprowdataform2 = []
        row = db.user.find(
            {
            "username" : username
            })
        for i in row:
            temprow.update(i)

        row_dataform1 = db.form1.find({
            "username" : username
        })

        for j in row_dataform1:
            temprowdataform1.append(j)

        row_dataform2 = db.form2.find({
            "username" : username
        })

        for k in row_dataform2:
            temprowdataform2.append(k)

        if bool(temprow) == True:
            if temprow["username"] == username and temprow["password"] == password:
                if temprow["flag"] == 1:
                    print(temprowdataform1)
                    return render_template('vlogin_mahasiswa.html', username = username, temprowdataform1 = temprowdataform1, temprowdataform2 = temprowdataform2)
                else:
                    return render_template('vlogin_tu.html')
            else:
                return render_template('vlogin_gagal.html')
        else:
            return render_template('vlogin_gagal.html')    
    else:
        return render_template('vlogin_user.html')

@app.route('/tambahForm1', methods = ['POST', 'GET'])
def tambahForm1():
    if request.method == 'POST':
        username = request.form['username']
        nrp = request.form['nrp']
        nama = request.form['nama']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        email = request.form['email']
        alamat_asal = request.form['alamat_asal']
        sks = request.form['sks']
        ipk = request.form['ipk']
        tanggal_proposal = request.form['tanggal_proposal']
        dospem_ta = request.form['dospem_ta']
        judul_ta = request.form['judul_ta']
        db.form1.insert_one(
                {
                "nrp": nrp,
                "nama":nama,
                "tempat_lahir":tempat_lahir,
                "tanggal_lahir":tanggal_lahir,
                "email": email,
                "alamat_asal":alamat_asal,
                "sks":sks,
                "ipk":ipk,
                "tanggal_proposal": tanggal_proposal,
                "dospem":dospem_ta,
                "judul_ta":judul_ta,
                "flag": 0,
                "time":datetime.datetime.now(),
                "username":username     
                })
        return redirect('http://localhost:5000')
    else:
        return render_template('vtambah_form1.html')
    

if __name__ == '__main__':
    app.run(debug=True)