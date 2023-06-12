# -*- coding: utf-8 -*-
"""21-048_Lu'luatul maknunah_UAS PENDATA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yARczFNOASb9jw-mV_UWDsYc7RB5iiiS
"""
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image


st.title('DEKARU(DETEKSI KANKER PARU-PARU)')
selected=option_menu(
    menu_title=None,
    options=['Data', 'Preproces','Model','Implementasi','Me'],
    default_index=0,
    orientation='horizontal',
    menu_icon=None,
    styles={
    "nav-link":{
        "font-size":"12px",
        "text-align":"center",
        "margin":"5px",
        "--hover-color":"#eee",},
    "nav-link-selected":{
        "background-color":"red"},
    })
dt= pd.read_csv('https://raw.githubusercontent.com/LuluatulMaknunah21-048/Pendata/main/survey-lung-cancer.csv')
if selected =='Data':
    """#**LOAD DATA**"""
    st.write('data di peroleh dari kaggle : https://www.kaggle.com/code/sandragracenelson/lung-cancer-prediction/input')
    st.write('Deskripsi Data :')
    st.write('Efektivitas sistem prediksi kanker membantu orang untuk mengetahui risiko kanker mereka dengan biaya rendah dan juga membantu orang untuk mengambil keputusan yang tepat berdasarkan status risiko kanker mereka. Data dikumpulkan dari situs web sistem prediksi kanker paru-paru online')
    st.write('Jumlah total atribut:16 Jumlah instance:284 Informasi atribut: 1. Jenis kelamin: M(pria), F(wanita) 2. Usia: Usia pasien 3. Merokok: YA = 2, TIDAK = 1. 4. Jari kuning: YA = 2, TIDAK = 1. 5. Kecemasan: YA = 2, TIDAK = 1. 6. Peer_pressure: YA = 2, TIDAK = 1. 7. Penyakit kronis: YA = 2, TIDAK = 1. 8. Kelelahan: YA = 2, TIDAK = 1. 9. Alergi: YA = 2, TIDAK = 1. 10. Mengi: YA = 2, TIDAK = 1. 11. Alkohol: YA = 2, TIDAK = 1. 12. Batuk: YA = 2, TIDAK = 1. 13. Sesak napas: YA = 2, TIDAK = 1. 14. Kesulitan menelan: YA = 2, TIDAK = 1. 15. Nyeri dada: YA = 2, TIDAK = 1. 16. Kanker Paru-paru: YA , TIDAK.')
    dt
    

if selected =='Preproces':
    """#**PRE-PROCESSING**"""
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import LabelEncoder
    from sklearn.utils import resample
    st.write('NORMALISASI DATA MENGGUNAKAN MIN-MAX')
    """# Mengubah kategorikal ke numerik"""
    # Mendapatkan daftar kolom pada dokumen
    kolom_kategorikal = ['GENDER']  # Ganti dengan daftar kolom kategorikal yang sesuai
    # Membuat objek LabelEncoder
    encoder = LabelEncoder()
    # Melakukan Label Encoding pada setiap kolom kategorikal
    for kolom in kolom_kategorikal:
        dt[kolom] = encoder.fit_transform(dt[kolom])
    # Menampilkan hasil
    dt
    """# Normalisasi data"""
    # Memilih kolom yang akan dinormalisasi
    columns_to_normalize = ["AGE","SMOKING","YELLOW_FINGERS","ANXIETY", "PEER_PRESSURE", "CHRONIC_DISEASE","FATIGUE","ALLERGY", "WHEEZING","ALCOHOL_CONSUMING", "COUGHING","SHORTNESS_OF_BREATH","SWALLOWING_DIFFICULTY","CHEST_PAIN"]
    # Membuat objek scaler Min-Max
    scaler = MinMaxScaler()
    # Melakukan normalisasi pada kolom yang dipilih
    dt[columns_to_normalize] = scaler.fit_transform(dt[columns_to_normalize])
    dt
    """# over sampling"""

    # Memisahkan data menjadi kelas mayoritas dan minoritas
    majority_class =dt[dt['LUNG_CANCER'] == 'YES']
    minority_class = dt[dt['LUNG_CANCER'] == 'NO']

    # Oversampling pada kelas minoritas
    oversampled_minority = resample(minority_class,
                                    replace=True,  # Memungkinkan penggantian pengamatan
                                    n_samples=len(majority_class),  # Menyesuaikan jumlah dengan kelas mayoritas
                                    random_state=42)  # Menetapkan seed untuk reproduktibilitas

    # Menggabungkan kelas mayoritas dengan kelas minoritas yang di-oversampling
    dt= pd.concat([majority_class, oversampled_minority])

    # Menampilkan data yang di-oversampling
    dt
    dt.to_csv('kankerparubersih.csv')
if selected=='Model':
    data=pd.read_csv('kankerparubersih.csv')
    y = data['LUNG_CANCER']
    x = data.drop(['LUNG_CANCER'], axis=1)
    genre = st.radio(
    "PILIH MODEL : ",
    ('ANN', 'NAIVE BAYES', 'KNN','DECISION TREE'))
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    if genre=='ANN':
        """#**KLASIFIKASI MENGGUNAKAN ANN**"""
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=21)
        clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=200, alpha=0.001,solver='sgd', verbose=10,  random_state=21,tol=0.001)
        clf.fit(x_train, y_train)
        y_pred=clf.predict(x_test)
        st.write('AKURASI ANN : ',accuracy_score(y_test, y_pred))
    if genre == 'NAIVE BAYES' :
        """#**KLASIFIKASI MENGGUNAKAN NAIVE BAYES**"""
        X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size= 0.2, random_state=21)
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB()
        classifier.fit(X_train, Y_train)
        Y_predi = classifier.predict(X_test) 
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(Y_test, Y_predi)
        from sklearn.metrics import accuracy_score 
        st.write("Accuracy NAIVE BAYES : ", accuracy_score(Y_test, Y_predi))
    if genre == 'KNN':
        """#**KLASIFIKASI KNN**"""
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=21)
        from sklearn.neighbors import KNeighborsClassifier
        classifierknn = KNeighborsClassifier(n_neighbors=5)
        classifierknn.fit(x_train, y_train)
        y_predik= classifierknn.predict(x_test) 
        from sklearn.metrics import confusion_matrix
        cmknn = confusion_matrix(y_test, y_predik)
        from sklearn.metrics import accuracy_score 
        st.write("Accuracy KNN : ", accuracy_score(y_test, y_predik))

    #import pickle
    #filename='kankerparu.pkl'
    #pickle.dump(classifierknn,open(filename,'wb'))

    #import os
    #print(os.getcwd())

    #from google.colab import files
    #files.download('kankerparu.pkl')
    if genre=='DECISION TREE':
        """#**KLASIFIKASI POHON KEPUTUSAN**"""

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 21)

        from sklearn.tree import DecisionTreeClassifier
        # instantiate the DecisionTreeClassifier model with criterion gini index
        clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=21)
        # fit the model
        clf_gini.fit(X_train, y_train)
        y_pred_gini = clf_gini.predict(X_test)
        from sklearn.metrics import accuracy_score
        st.write('Model accuracy POHON KEPUTUSAN: ',accuracy_score(y_test, y_pred_gini))
if selected=='Implementasi':
    col1,col2=st.columns(2)
    status=['Silahkan pilih','Ya','Tidak']
    gend=['Silahkan pilih','FEMALE','MALE']
    SWALLOWING_DIFFICULTY=st.selectbox('Apakah Anda mengalami kesulitan menelan makanan atau minuman ? ',status)
    if SWALLOWING_DIFFICULTY == 'Tidak':
        SWALLOWING_DIFFICULTY=0
    if SWALLOWING_DIFFICULTY == 'Ya':
        SWALLOWING_DIFFICULTY= 1
    with col1:
        AGE=st.number_input('USIA',0)
        GENDER=st.selectbox('Jenis Kelamin ',gend)
        if GENDER == 'FEMALE':
            GENDER=0
        if GENDER == 'MALE':
            GENDER= 1
        SMOKING=st.selectbox('Apakah anda merokok ? ',status)
        if SMOKING == 'Tidak':
            SMOKING=0
        if SMOKING == 'Ya':
            SMOKING= 1
        YELLOW_FINGERS=st.selectbox('Apakah Kuku Jari anda menguning ? ',status)
        if YELLOW_FINGERS == 'Tidak':
            YELLOW_FINGERS=0
        if YELLOW_FINGERS == 'Ya':
            YELLOW_FINGERS= 1
        ANXIETY=st.selectbox('Apakah Anda sering merasa cemas? ',status)
        if ANXIETY == 'Tidak':
            ANXIETY=0
        if ANXIETY == 'Ya':
            ANXIETY= 1
        PEER_PRESSURE=st.selectbox('Apakah anda mudah terpengaruh oleh lingkungan ? ',status)
        if PEER_PRESSURE == 'Tidak':
            PEER_PRESSURE=0
        if PEER_PRESSURE == 'Ya':
            PEER_PRESSURE= 1
        CHRONIC_DISEASE=st.selectbox('Apakah anda menderita penyakit kronis ? ',status)
        if CHRONIC_DISEASE == 'Tidak':
            CHRONIC_DISEASE=0
        if CHRONIC_DISEASE == 'Ya':
            CHRONIC_DISEASE= 1
    with col2:
        FATIGUE=st.selectbox('Apakah anda sering merasa lelah ? ',status)
        if FATIGUE == 'Tidak':
            FATIGUE=0
        if FATIGUE == 'Ya':
            FATIGUE= 1
        ALLERGY=st.selectbox('Apakah Memiliki riwayat alergi ? ',status)
        if ALLERGY == 'Tidak':
            ALLERGY=0
        if ALLERGY == 'Ya':
            ALLERGY= 1
        WHEEZING=st.selectbox('Apakah anda sering sesak nafas bersuara atau mengi? ',status)
        if WHEEZING == 'Tidak':
            WHEEZING=0
        if WHEEZING == 'Ya':
            WHEEZING= 1
        ALCOHOL_CONSUMING=st.selectbox('Apakah anda mengonsumsi alkohol ? ',status)
        if ALCOHOL_CONSUMING == 'Tidak':
            ALCOHOL_CONSUMING=0
        if ALCOHOL_CONSUMING == 'Ya':
            ALCOHOL_CONSUMING= 1
        COUGHING=st.selectbox('Apakah anda mengalami batuk yang berlangsung lama ? ',status)
        if COUGHING == 'Tidak':
            COUGHING=0
        if COUGHING == 'Ya':
            COUGHING= 1
        SHORTNESS_OF_BREATH=st.selectbox('Apakah anda merasa sesak nafas atau sulit bernafas ? ',status)
        if SHORTNESS_OF_BREATH == 'Tidak':
            SHORTNESS_OF_BREATH=0
        if SHORTNESS_OF_BREATH == 'Ya':
            SHORTNESS_OF_BREATH= 1
        CHEST_PAIN=st.selectbox('Apakah anda sering mengalami nyeri dada ? ',status)
        if CHEST_PAIN == 'Tidak':
            CHEST_PAIN=0
        if CHEST_PAIN == 'Ya':
            CHEST_PAIN= 1
    button=st.button('Deteksi',use_container_width=500,type='primary')
    if button:
        if AGE != 0 and GENDER != 'Silahkan pilih' and SMOKING !='Silahkan pilih' and YELLOW_FINGERS !='Silahkan pilih' and ANXIETY !='Silahkan pilih' and PEER_PRESSURE !='Silahkan pilih' and CHRONIC_DISEASE !='Silahkan pilih'and FATIGUE !='Silahkan pilih' and ALLERGY !='Silahkan pilih'and WHEEZING!='Silahkan pilih' and ALCOHOL_CONSUMING!='Silahkan pilih'and COUGHING!='Silahkan pilih' and SHORTNESS_OF_BREATH !='Silahkan pilih' and SWALLOWING_DIFFICULTY !='Silahkan pilih' and CHEST_PAIN !='Silahkan pilih':
            import pickle
            with open('kankerparu.pkl','rb') as r:
                kanker=pickle.load(r)
            AGE=((AGE-21)/(87-21))*(1-0)+0
            #st.write(GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE,FATIGUE,ALLERGY, WHEEZING,ALCOHOL_CONSUMING, COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN)
            
            deteksi=kanker.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE,FATIGUE,ALLERGY, WHEEZING,ALCOHOL_CONSUMING, COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
            for detect in deteksi:
                if detect == 'YES':
                    st.write('Status : ',detect,', Karena Dari gejala yang anda alami diagnosa anda TERKONFIRMASI KANKER PARU-PARU, silahkan periksakan diri anda ke dokter untuk tindakan lebih lanjut')
                if detect =='NO':
                    st.write('Status : ',detect,', Anda tidak mengidap Kanker Paru')
        else:
            st.write('Mohon Isi semua Kolom Pertanyaan')
if selected=='Me':
    st.write("Nama : Lu'luatul Maknunah")
    st.write('NIM : 210411100048')
    st.write('KELAS : Penambangan Data B')
