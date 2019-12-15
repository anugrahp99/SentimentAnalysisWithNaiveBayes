#Amelia Kosasih - 175150200111027
#Anugrah Prasetia - 175150200111004
#Griselda Anjeli Sirait - 175150200111002

#Regular expression (regex) adalah deretan karakter yang digunakan untuk pencarian string atau teks dengan menggunakan pola (pattern). 
import re #library Regular Expression untuk hapusAngka
import string #library string untuk hapusTandaBaca
import csv as c #Library csv untuk mengakses file csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #library Sastrawi untuk Stemming

#Method untuk Parsing
def bacaDokumen(dok):
    dokumen = open(dok,"r") #r: membaca
    isi = dokumen.read()
    dokumen.close()
    hasil = isi
    return hasil
    
#Method untuk Tokenisasi
def tokenisasi(dok):
    pisah = dok.split()
    hasil = pisah
    return hasil

#Method untuk Case Folding dan Penghilangan angka, tanda baca, karakter
def caseFolding(dok):
    hurufKecil = dok.lower()
    hapusAngka = re.sub(r"\d+", "", hurufKecil)
    hapusTandaBaca = hapusAngka.translate(str.maketrans("","",string.punctuation))
    hapusWhiteSpace = hapusTandaBaca.strip()
    hasil = hapusWhiteSpace
    return hasil

#Method untuk Cleaning = tidak ada

#Stopword dari Fadillah Z Tala -> https://www.kaggle.com/oswinrh/indonesian-stoplist
def stopword():
    sw=[]
    with open('stopwordbahasa.csv') as File:
        reader = c.reader(File)
        for row in reader:
            str1 = "".join(row)
            sw.append(str1)
    File.close()
    return sw

#Method untuk Filtering    
def filtering(dok):
    hasil=[]
    sw = stopword()
    for word in dok:
        if word not in sw:
            str = "".join(word)
            hasil.append(str)
    return hasil;

#Method untuk Stemming -> Python Sastrawi (Stemming Bahasa Indonesia)
def stemming(dok):
    hasil=[]
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    for word in dok:
        output = stemmer.stem(word)
        hasil.append(output)
    return hasil

#Method untuk Preprocessing
def preprocessing(dok):
    tahap1 = caseFolding(dok)
    tahap2 = tokenisasi(tahap1)
    tahap3 = filtering(tahap2)
    tahap4 = stemming(tahap3)
    return tahap4

#Untuk menyimpan hasil pemrosesan ke .csv
def writefilecsv(dok,namaDok):
    with open(namaDok, 'a+',newline='') as csvfile:
        filewriter = c.writer(csvfile)
        filewriter.writerow(dok)
    csvfile.close()    
    
#Method running untuk menhjalankan proses Preprocessing lalu disimpan hasilnya ke dalam .csv
def RUN():
    with open('dokumenUlasanBaru.csv') as File:
        reader = c.reader(File)
        for row in reader:
            baris= "".join(row)
            writefilecsv(preprocessing(baris),'hasilPreProcessingBaru.csv')

def Testing():
    hasil = []
    with open('dokumenTesting.csv') as File:
        reader = c.reader(File)
        for row in reader:
            baris= "".join(row)
            hasil.append(preprocessing(baris))
    return hasil
#Menjalankan method RUN()

#output : membuat file hasilProcessing.csv yang berisi hasil preprocessing dari dokumenUlasan.csv