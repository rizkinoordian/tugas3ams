import pandas as pd
import pickle

# fungsi untuk load dataset
def load_dataset(filename):
    # kita load training data untuk membentu model classification
    # header = -1 jika tidak ada header, 0 jika ada header
    dataFrame = pd.read_csv(filename, header = -1)

    # ubah format dataFrame panda ke bentuk numpy array
    # library sklearn hanya memproses dataset dalam bentuk numpy array
    dataArray = dataFrame.values
    return dataArray

# fungsi untuk save learned model ke sebuah file
def save_model(model, filename):
    # Kita simpan model yang sudah dilatih ke sebuah file, dengan library Pickle
    # library untuk serialisasi di python
    pickle.dump(model, open(filename, 'wb'))

# fungsi untuk load kembali model yang sudah di-save pada suatu file
def load_model(filename):
    # Kita muat kembali model yang sudah kita latih sebelumnya
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model