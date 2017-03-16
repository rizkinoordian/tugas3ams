from __future__ import print_function

import numpy as np

from util import load_dataset, save_model, load_model

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from sklearn import preprocessing


# Goal: diberikan labeled training data, kita ingin bangun model klasifikasi

# kita load training data untuk membentu model classification
# dataArray dalam bentuk numpy array 2D (num_sample x num_feature)
dataArray = load_dataset('./datasets/train.gender.data')

# kita pisah antara Fitur dan Class
# X merupakan kumpulan fitur untuk setiap instance, kolom indeks 1 - 9
# Y merupakan label dari setiap instance, kolom indeks
# Y adalah vector of integers or strings.

# split data menjadi train dan test
dataArray_train, dataArray_test = train_test_split(dataArray, test_size=0.5)

X_train = dataArray_train[:, 1:10]
Y_train = dataArray_train[:, 10]

# Kita gunakan Algoritma Machine Learning Logistic Regression
# untuk membangun model
model_DTC = DecisionTreeClassifier()
model_GNB = GaussianNB()
model_LR = LogisticRegression()

# Training ! proses ini akan membutuhkan waktu, untuk estimasi parameter
# tidak perlu disimpan karena menggunakan file yang sama
model_DTC.fit(X_train, Y_train)
model_GNB.fit(X_train, Y_train)
model_LR.fit(X_train, Y_train)

# -==Eval==-
# Goal: Kita ingin evaluasi seberapa baik performa klasifikasi model kita?

X_test = dataArray_test[:, 1:10]
Y_test = dataArray_test[:, 10]

# beri label testing data terlebih dahulu
Y_predicted_dtc = model_DTC.predict(X_test)
Y_predicted_gnb = model_GNB.predict(X_test)
Y_predicted_lr = model_LR.predict(X_test)

# hitung score, bandingkan hasil label prediksi, dengan label sesungguhnya
# di testing data
# --> tampilkan nilai accuracy
accuracy_dtc = accuracy_score(Y_test, Y_predicted_dtc)
accuracy_gnb = accuracy_score(Y_test, Y_predicted_gnb)
accuracy_lr = accuracy_score(Y_test, Y_predicted_lr)

# menentukan model mana yang terbaik
best_model = model_DTC
if accuracy_dtc < accuracy_gnb:
    best_model = model_GNB
    if accuracy_gnb < accuracy_lr:
        best_model = model_LR
        print ('we are using LR with accuracy: ', accuracy_lr)
        pass
    print ('we are using GNB with accuracy: ', accuracy_gnb)
elif accuracy_dtc < accuracy_lr:
    best_model = model_LR
    print ('we are using LR with accuracy: ', accuracy_lr)

if best_model == model_DTC:
    print ('we are using DTC with accuracy: ', accuracy_dtc)

# -==Predict==-
# Goal: Kita ingin menggunakan model yang sudah dibuat untuk prediksi
# sebuah instance

# kita coba prediksi test file, yang belum diketahui labelnya
test_data = load_dataset('./datasets/test.gender.nolabel.data')
test_data = test_data[:, 1:10]

# hasil prediksi ada di variable predicted_class
predicted_class = best_model.predict(test_data)

# convert numpy array to text
np.savetxt('./predictresult/hasil.txt', predicted_class, fmt='%s')
