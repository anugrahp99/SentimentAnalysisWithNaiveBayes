#Amelia Kosasih - 175150200111027
#Anugrah Prasetia - 175150200111004
#Griselda Anjeli Sirait - 175150200111002

import csv as c
import numpy as np
import Pembobotan
import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#from matplotlib.mlab import PCA

def ConfusionMatrix(true,pred):
    return confusion_matrix(true, pred, labels=["Positif", "Negatif"])
    
def countAccuracy(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    c = confusionMtx[1][0]
    d = confusionMtx[1][1]
    accuracy = (a+d)/(a+b+c+d)
    return accuracy 

def countPrecision(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    precision = (a)/(a+b)
    return precision    

def countRecall(confusionMtx):
    a = confusionMtx[0][0]
    c = confusionMtx[1][0]
    recall = (a)/(a+c)
    return recall

def bacaDokumen(dok):
#    dokumen = open(dok,"r",encoding='utf-8-sig') #r: membaca
#    hasil = dokumen.read()
    hasil=[]
    with open(dok,"r",encoding='utf-8-sig') as File:
        reader = c.reader(File)
        for word in reader:
            hasil.append(word)
    return hasil

def countPosterior(prior,likelihood,evidence):
    return prior*likelihood/evidence

def getKelas(data):
    return max(data)

def multinomial(datac,termunik,wdatac):
    return (wdatac+1)/(datac+abs(termunik))

def getPembobotan(namaDok):
    mtxPembobotan=[]
    with open(namaDok) as File:
        reader = c.reader(File)
        for word in reader:
            mtxPembobotan.append(word)
    return mtxPembobotan

def seperateByClass(data,kelas,tipe):
    hasil = []
    dataArray = np.array(data)
    for x in range(0,len(kelas)):
        if kelas[x][0] == str(tipe):
            hasil.append(dataArray[:,(x+1)].tolist())
    return hasil

def countCategory(data):
    total= 0
    for x in data:
        castedList = list(map(float,x))
        total += sum(castedList)
    return total

def countLikelihood(data,termUnik,countCategory):
    hasil = []
    dataArray = np.array(data)
    for x in range(0,termUnik):
        castedList = list(map(float,dataArray[:,x].tolist()))
        jumlahKejadianFitur = sum(castedList)
        likelihoodfitur = multinomial(countCategory,termUnik,jumlahKejadianFitur)
        hasil.append(likelihoodfitur)
    return hasil

def countPrior(kelas,tipe):
    hasil = 0
    for x in range(0,len(kelas)):
        if kelas[x][0] == str(tipe):
            hasil += 1
    return hasil/len(kelas)

def countPosteriorTesting(data,index):
    return 1

def getIndexOfTestingDok(dokTesting,term):
    index = []
    for x in dokTesting:
        tempHasil = []
        for y in x:
            elemenIndex = term.index(y) if y in term else -1
            if elemenIndex != -1:
                tempHasil.append(elemenIndex)
        index.append(tempHasil)
    return index

def Testing(likelihoodPositif,likelihoodNegatif,priorPositif,priorNegatif,index):
    hasil=[]
    i=1
    for x in index:
        hasilPositif = priorPositif
        hasilNegatif = priorNegatif
        for y in x:
            hasilPositif *= likelihoodPositif[y]
            hasilNegatif *= likelihoodNegatif[y]
        result = hasilPositif > hasilNegatif
        hasil.append("Positif" if result else "Negatif")
        i+=1
    return hasil
    

def KlasifikasiNB():
    #Get Hasil Pembobotan menggunakan module pembobotan
    hasilPembobotan1 = Pembobotan.RUN()
    #Get term unik untuk variabel |V|
    termUnik = 3
    
    #PCA
    hasilPembobotan = np.array(hasilPembobotan1).transpose()
    hasilPembobotan = np.delete(hasilPembobotan, (0), axis=0)
    hasilPembobotan = StandardScaler().fit_transform(hasilPembobotan)
    pca = PCA(n_components=3)
    principalComponents = pca.fit_transform(hasilPembobotan)
    fitur = []
    fitur.append(['fitur1','fitur2','fitur3'])
    hasilPembobotan = ((np.concatenate((fitur,principalComponents))).transpose()).tolist()
    #Get label dari data training
    kelas = bacaDokumen("labelDataTraining3.csv")
    
    #Memisahkan berdasarkan label yang sudah ada (Negatif / Positif)
    dataPositif = seperateByClass(hasilPembobotan,kelas,1)
    dataNegatif = seperateByClass(hasilPembobotan,kelas,0)
    
    #Menghitung jumlah kejadian Positif/Negatif
    countPositif = countCategory(dataPositif)
    countNegatif = countCategory(dataNegatif)
    
    #Menghitung Likelihood
    likelihoodPositif = countLikelihood(dataPositif,termUnik,countPositif)
    likelihoodNegatif = countLikelihood(dataNegatif,termUnik,countNegatif)

    #Menghitung prior dari masing masing kelas
    priorPositif = countPrior(kelas,1)
    priorNegatif = countPrior(kelas,0)
   
    #Get data testing dan dilakukan preprocessing terlebih dahulu
    dokTesting = preprocessing.Testing()
    
    #Mendapatkan Index dari tiap fitur pada masing masing dokumen
    indexTesting = getIndexOfTestingDok(dokTesting,np.array(hasilPembobotan)[:,0].tolist())
    
    #Melakukan klasifikasi terhadap data testing
    hasilTesting = Testing(likelihoodPositif,likelihoodNegatif,priorPositif,priorNegatif,indexTesting)
    print(hasilTesting)
    
    #Set hasil yang diharapkan terhadap hasil klasifikasi
    true = ['Positif', 'Negatif']
    
    #Membuat confusion matrix dengan membandingkan hasil klasifikasi dengan prediksi
    confusionMtx = ConfusionMatrix(hasilTesting,true)
    print(confusionMtx)
    #Menghitung akurasi berdasarkan hasil confusi matrik
    accuracy = countAccuracy(confusionMtx)
    recall = countRecall(confusionMtx)
    precision = countPrecision(confusionMtx)
    print(accuracy*100)
    print(recall*100)
    print(precision*100)

KlasifikasiNB()
    
    

    