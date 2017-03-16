from util import load_dataset, save_model, load_model
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Goal: Kita ingin evaluasi seberapa baik performa klasifikasi model kita?

# load testing data
dataArray = load_dataset('./datasets/train.gender.data')

X_test = dataArray[:,1:10]
Y_test = dataArray[:,10] #label yang sebenarnya

# Kita muat kembali model yang sudah kita latih sebelumnya
loaded_model = load_model('lr.model')

# beri label testing data terlebih dahulu
Y_predicted = loaded_model.predict(X_test)

##### metrics evaluasi #####
# hitung score, bandingkan hasil label prediksi, dengan label sesungguhnya di testing data
# --> tampilkan nilai accuracy
accuracy = accuracy_score(Y_test, Y_predicted)
print 'accuracy : ', accuracy

# --> metric lebih detail: precision, recall, f1
report = classification_report(Y_test, Y_predicted)
print '\nprecision, recall, f1:'
print report

# --> confusion matrix
print '\nconfusion matrix:'
print confusion_matrix(Y_test, Y_predicted)
