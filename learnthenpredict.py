from __future__ import print_function

import numpy as np

from util import load_dataset, save_model, load_model

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from sklearn import preprocessing


# Goal: diberikan labeled training data, kita ingin bangun model klasifikasi

# kita load training data untuk membentu model classification
# dataArray dalam bentuk numpy array 2D (num_sample x num_feature)
dataArray = load_dataset('./train.gender.data')

# kita pisah antara Fitur dan Class
# X merupakan kumpulan fitur untuk setiap instance, kolom indeks 1 - 9
# Y merupakan label dari setiap instance, kolom indeks
# Y adalah vector of integers or strings.
X_train = dataArray[:,1:10]
Y_train = dataArray[:,10]

# Kita gunakan Algoritma Machine Learning Logistic Regression untuk membangun model
model_DTC = DecisionTreeClassifier()
model_GNB = GaussianNB()
model_LR = LogisticRegression()

# Training ! proses ini akan membutuhkan waktu, untuk estimasi parameter
model_DTC.fit(X_train, Y_train)
model_GNB.fit(X_train, Y_train)
model_LR.fit(X_train, Y_train)

# Kita simpan model yang sudah dilatih ke sebuah file
save_model(model_DTC, 'dtc.model')
save_model(model_GNB, 'gnb.model')
save_model(model_LR, 'lr.model')

# Goal: Kita ingin menggunakan model yang sudah dibuat untuk prediksi sebuah instance

# Kita muat kembali model yang sudah kita latih sebelumnya
loaded_model_dtc = load_model('dtc.model')
loaded_model_gnb = load_model('gnb.model')
loaded_model_lr = load_model('lr.model')

# kita coba prediksi test file, yang belum diketahui labelnya
test_data = load_dataset('./test.gender.nolabel.data')
test_data = test_data[:,1:10]

# with open('debug.txt', 'w') as f:
#     print(test_data, file=f)

# hasil prediksi ada di variable predicted_class
predicted_class = loaded_model_dtc.predict(test_data)

# convert numpy array to text
np.savetxt('hasil.txt', predicted_class, fmt='%s')
