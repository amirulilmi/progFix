from flask import Flask, render_template, request, flash, redirect, url_for, session
import pandas as pd
import numpy as np
import re
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pickle

# Load model
model_path = 'trained.h5'
model = load_model(model_path)

# Load scaler
scaler_path = 'fitted_scaler.pkl'
with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

app = Flask(__name__, static_url_path='')
app.secret_key = 'secret_key'  # Kunci rahasia untuk pesan flash


@app.route('/')
def index():
    return render_template('cek_gejala.html')

@app.route('/submit', methods=['POST'])
def submit():
    # model = 'C:/laragon/www/progFIX/trained_model.h5'
    if request.method == 'POST':
        nama = request.form['nama']
        usia = request.form['usia']
        gender = request.form['gender']
        p1 = int(request.form['pilihan1'])
        p2 = int(request.form['pilihan2'])
        p3 = int(request.form['pilihan3'])
        p4 = int(request.form['pilihan4'])
        p5 = int(request.form['pilihan5'])
        p6 = int(request.form['pilihan6'])
        p7 = int(request.form['pilihan7'])
        p8 = int(request.form['pilihan8'])
        p9 = int(request.form['pilihan9'])
        p10 = int(request.form['pilihan10'])
        p11 = int(request.form['pilihan11'])
        p12 = int(request.form['pilihan12'])

        # input_values = []

        # input_values.append(p1)
        # input_values.append(p2)
        # input_values.append(p3)
        # input_values.append(p4)
        # input_values.append(p5)
        # input_values.append(p6)
        # input_values.append(p7)
        # input_values.append(p8)
        # input_values.append(p9)
        # input_values.append(p10)
        # input_values.append(p11)
        # input_values.append(p12)

        
        # # Tambahkan satu fitur tambahan yang kosong
        # input_values.append(0)  # Misalnya, kita tambahkan nilai 0 untuk fitur ke-13 yang tidak ada
        # input_array = np.array(input_values).reshape(1, 1, 13)  # Reshape sesuai dengan format yang diperlukan oleh model

        # # Lakukan prediksi
        # predicted_prob = model.predict(input_array)
        # predicted_class = np.argmax(predicted_prob)

        # y  = input_values  
        # label_encoder = LabelEncoder()
        # label_encoder.fit(y)
        # # Decode label prediksi

        
        x = p1 + p2 + p3 + p4 + p5 + p6
        y = p7 + p8 + p9 + p10 + p11 + p12

        # Standarkan fitur input yang ingin Anda prediksi
        X_new = scaler.transform([[x, y]])

        # Buat prediksi menggunakan model
        predictions = model.predict(X_new)

        # Interpretasikan hasil prediksi
        predicted_class = np.argmax(predictions)

        # predicted_label = label_encoder.inverse_transform([predicted_class])[0]

        return render_template('hasil.html', nama=nama,usia=usia, gender=gender, predict=predicted_class)

if __name__ == "__main__":
    app.run()
