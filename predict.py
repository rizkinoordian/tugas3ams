from __future__ import print_function

import numpy as np

from util import load_dataset, save_model, load_model

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

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
dataArray_train, dataArray_test = train_test_split(dataArray, test_size=0.27)

X_train = dataArray_train[:, 1:10]
Y_train = dataArray_train[:, 10]

# Kita gunakan Algoritma Machine Learning Logistic Regression
# untuk membangun model
model_DTC = DecisionTreeClassifier()
model_GNB = GaussianNB()
model_LR = LogisticRegression()
model_MLP = MLPClassifier(solver='adam', hidden_layer_sizes=(100, 10, 5))

# Training ! proses ini akan membutuhkan waktu, untuk estimasi parameter
# tidak perlu disimpan karena menggunakan file yang sama
model_DTC.fit(X_train, Y_train)
model_GNB.fit(X_train, Y_train)
model_LR.fit(X_train, Y_train)
model_MLP.fit(X_train, Y_train)

# -==Eval==-
# Goal: Kita ingin evaluasi seberapa baik performa klasifikasi model kita?

X_test = dataArray_test[:, 1:10]
Y_test = dataArray_test[:, 10]

# beri label testing data terlebih dahulu
Y_predicted_dtc = model_DTC.predict(X_test)
Y_predicted_gnb = model_GNB.predict(X_test)
Y_predicted_lr = model_LR.predict(X_test)
Y_predicted_mlp = model_MLP.predict(X_test)

# hitung score, bandingkan hasil label prediksi, dengan label sesungguhnya
# di testing data
# --> tampilkan nilai accuracy
accuracy_dtc = accuracy_score(Y_test, Y_predicted_dtc)
accuracy_gnb = accuracy_score(Y_test, Y_predicted_gnb)
accuracy_lr = accuracy_score(Y_test, Y_predicted_lr)
accuracy_mlp = accuracy_score(Y_test, Y_predicted_mlp)

# menentukan model mana yang terbaik
# best_model = model_DTC
# if accuracy_dtc < accuracy_gnb:
#     best_model = model_GNB
#     if accuracy_gnb < accuracy_lr:
#         best_model = model_LR
#         print ('we are using LR!')
#         pass
#         if accuracy_lr < accuracy_mlp:
#             best_model = model_MLP
#             print ('we are using MLP!')
#             pass
#         pass
#     elif accuracy_gnb < accuracy_mlp:
#         best_model = model_MLP
#         print ('we are using MLP!')
#         pass
#     print ('we are using GNB!')
# elif accuracy_dtc < accuracy_lr:
#     best_model = model_LR
#     print ('we are using LR!')
# elif accuracy_dtc < accuracy_mlp:
#     best_model = model_MLP
#     print ('we are using MLP!')


print ('accuracy (DT, GNB, LR, MLP): ({0}, {1}, {2}, {3})'
       .format(accuracy_dtc, accuracy_gnb, accuracy_lr, accuracy_mlp))

user_choice = raw_input('choose your model (A, B, C, etc): ')

choosen_model = model_DTC
if user_choice is 'B':
    choosen_model = model_GNB
    print('we are using GNB')
elif user_choice is 'C':
    choosen_model = model_LR
    print('we are using LR')
elif user_choice is 'D':
    choosen_model = model_MLP
    print('we are using MLP')
else:
    print('we are using DTC')

# -==Predict==-
# Goal: Kita ingin menggunakan model yang sudah dibuat untuk prediksi
# sebuah instance

# kita coba prediksi test file, yang belum diketahui labelnya
test_data = load_dataset('./datasets/test.gender.nolabel.data')
test_data = test_data[:, 1:10]

# hasil prediksi ada di variable predicted_class
predicted_class = choosen_model.predict(test_data)

# convert numpy array to text
np.savetxt('./predictresult/hasil.txt', predicted_class, fmt='%s')
