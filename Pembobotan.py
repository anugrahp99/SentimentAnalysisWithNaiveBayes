#Amelia Kosasih - 175150200111027
#Anugrah Prasetia - 175150200111004
#Griselda Anjeli Sirait - 175150200111002

import csv as c
import numpy as np
from xlwt import Workbook 

#menghapus duplicate word
def nonDup(dok): 
    kata = []
    for data in dok:
        if data not in kata:
            kata.append(data)
    return kata
#mencari term dari seluruh dokumen
def term(namadok):
    terms=[]
    with open(namadok) as File:
        reader = c.reader(File)
        for word in reader:
            kata2 = nonDup(word)
            if word not in terms:
                terms+=kata2        
    terms=nonDup(terms)
    File.close()
    return terms

#membuka hasil preprocessing
def getPreprocessing(namadok):
    term=[]
    with open(namadok) as File:
        reader = c.reader(File)
        for word in reader:
            term.append(word)
    return term

#menghitung raw tf
def rawTF(term,dok):
    hasil=[]
    a=0
    for word in term:
        hasil.append([])
        for row in dok:
            sama = 0
            for kata in row:
                if kata == word:
                    sama +=1
            hasil[a].append(sama)
        a+=1
    return hasil

#Menghitung log term Frequency
def logTF(rawtf):
    hasil=[]
    a=0
    for row in rawtf:
        hasil.append([])
        for val in row:
            if val != 0:
                ltf = 1+np.log10(val)
                hasil[a].append(ltf)
            else:
                hasil[a].append(0)
        a+=1
    return hasil

#Menghitung document frequency
def docFreq(rawtf):
    hasil=[]
    for row in rawtf:
        sama=0
        for val in row:
            if val != 0:
                sama +=1
        hasil.append(sama)
    return hasil

#Menghitung inverse Document Frequency                
def inverseDF(df,n):
    hasil= []
    for val in df:
        idf = np.log10(n/val)
        hasil.append(idf)
    return hasil

#Menghitung TFIDF
def tfidf(tf,idf):
    hasil=[]
    a=0
    for row in tf:
        hasil.append([])
        for val in row:
            hasiltfidf = idf[a] * val
            hasil[a].append(hasiltfidf)
        a+=1
    return hasil

# Menyimpan hasil ke dalam file excel
def writehasilexcel(hasil):
    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1') 
    a=0
    sheet1.write(a,0,"Term")
    for b in range(1,31):
        sheet1.write(a,b,"Hasil TF D"+str(b))
    i=0
    for b in range(31,61):
        sheet1.write(a,b,"Hasil Log TF D"+str(i+1))
        i=i+1
    sheet1.write(a,61,"Hasil DF")
    sheet1.write(a,62,"Hasil IDF")
    i=0
    for b in range(63,93):
        sheet1.write(a,b,"Hasil TF-IDF D"+str(i+1))
        i=i+1
    for x in hasil:
        b=0
        a=a+1
        for y in x:
            sheet1.write(a,b,y)
            b=b+1
    wb.save('HasilPembobotanBaru.xls')

# Menyimpan hasil ke dalam file csv
def writehasilcsv(hasil):
   with open("HasilPembobotanBaru.csv", 'w+',newline='') as csvfile:
        fieldnames = ['term','hasil TF D1','hasil TF D2','hasi TF D3','hasil TF D4','hasil TF D5','hasi TF D6','hasil TF D7','hasil TF D8','hasi TF D9','hasil TF D10','hasil TF D11','hasi TF D12','hasi TF D13','hasil TF D14','hasil TF D15','hasi TF D16','hasil TF D17','hasil TF D18','hasi TF D19','hasil TF D20','hasil TF D21','hasi TF D22','hasi TF D23','hasil TF D24','hasil TF D25','hasi TF D26','hasil TF D27','hasil TF D28','hasi TF D29','hasil TF D30','hasil Log TF D1','hasil Log TF D2','hasi Log TF D3','hasil Log TF D4','hasil Log TF D5','hasi Log TF D6','hasil Log TF D7','hasil Log TF D8','hasi Log TF D9','hasil Log TF D10','hasil Log TF D11','hasi Log TF D12','hasi Log TF D13','hasil Log TF D14','hasil Log TF D15','hasi Log TF D16','hasil Log TF D17','hasil Log TF D18','hasi Log TF D19','hasil Log TF D20','hasil Log TF D21','hasi Log TF D22','hasi Log TF D23','hasil Log TF D24','hasil Log TF D25','hasi Log TF D26','hasil Log TF D27','hasil Log TF D28','hasi Log TF D29','hasil Log TF D30','hasil DF', 'hasil IDF','hasil TF-IDF D1','hasil TF-IDF D2','hasil TF-IDF D3','hasil TF-IDF D4','hasil TF-IDF D5','hasil TF-IDF D6','hasil TF-IDF D7','hasil TF-IDF D8','hasil TF-IDF D9','hasil TF-IDF D10','hasil TF-IDF D11','hasil TF-IDF D12','hasil TF-IDF D13','hasil TF-IDF D14','hasil TF-IDF D15','hasil TF-IDF D16','hasil TF-IDF D17','hasil TF-IDF D18','hasil TF-IDF D19','hasil TF-IDF D20','hasil TF-IDF D21','hasil TF-IDF D22','hasil TF-IDF D23','hasil TF-IDF D24','hasil TF-IDF D25','hasil TF-IDF D26','hasil TF-IDF D27','hasil TF-IDF D28','hasil TF-IDF D29','hasil TF-IDF D30']
        filewriter = c.DictWriter(csvfile,fieldnames=fieldnames)
        filewriter.writeheader()
        for row in hasil:
            filewriter.writerow({'term':row[0],'hasil TF D1':row[1],'hasil TF D2':row[2],'hasi TF D3':row[3],'hasil TF D4':row[4],'hasil TF D5':row[5],'hasi TF D6':row[6],'hasil TF D7':row[7],'hasil TF D8':row[8],'hasi TF D9':row[9],'hasil TF D10':row[10],'hasil TF D11':row[11],'hasi TF D12':row[12],'hasi TF D13':row[13],'hasil TF D14':row[14],'hasil TF D15':row[15],'hasi TF D16':row[16],'hasil TF D17':row[17],'hasil TF D18':row[18],'hasi TF D19':row[19],'hasil TF D20':row[20],'hasil TF D21':row[21],'hasi TF D22':row[22],'hasi TF D23':row[23],'hasil TF D24':row[24],'hasil TF D25':row[25],'hasi TF D26':row[26],'hasil TF D27':row[27],'hasil TF D28':row[28],'hasi TF D29':row[29],'hasil TF D30':row[30],'hasil Log TF D1':row[31],'hasil Log TF D2':row[32],'hasi Log TF D3':row[33],'hasil Log TF D4':row[34],'hasil Log TF D5':row[35],'hasi Log TF D6':row[36],'hasil Log TF D7':row[37],'hasil Log TF D8':row[38],'hasi Log TF D9':row[39],'hasil Log TF D10':row[40],'hasil Log TF D11':row[41],'hasi Log TF D12':row[42],'hasi Log TF D13':row[43],'hasil Log TF D14':row[44],'hasil Log TF D15':row[45],'hasi Log TF D16':row[46],'hasil Log TF D17':row[47],'hasil Log TF D18':row[48],'hasi Log TF D19':row[49],'hasil Log TF D20':row[50],'hasil Log TF D21':row[51],'hasi Log TF D22':row[52],'hasi Log TF D23':row[53],'hasil Log TF D24':row[54],'hasil Log TF D25':row[55],'hasi Log TF D26':row[56],'hasil Log TF D27':row[57],'hasil Log TF D28':row[58],'hasi Log TF D29':row[59],'hasil Log TF D30':row[60],'hasil DF':row[61], 'hasil IDF':row[62],'hasil TF-IDF D1':row[63],'hasil TF-IDF D2':row[64],'hasil TF-IDF D3':row[65],'hasil TF-IDF D4':row[66],'hasil TF-IDF D5':row[67],'hasil TF-IDF D6':row[68],'hasil TF-IDF D7':row[69],'hasil TF-IDF D8':row[70],'hasil TF-IDF D9':row[71],'hasil TF-IDF D10':row[72],'hasil TF-IDF D11':row[73],'hasil TF-IDF D12':row[74],'hasil TF-IDF D13':row[75],'hasil TF-IDF D14':row[76],'hasil TF-IDF D15':row[77],'hasil TF-IDF D16':row[78],'hasil TF-IDF D17':row[79],'hasil TF-IDF D18':row[80],'hasil TF-IDF D19':row[81],'hasil TF-IDF D20':row[82],'hasil TF-IDF D21':row[83],'hasil TF-IDF D22':row[84],'hasil TF-IDF D23':row[85],'hasil TF-IDF D24':row[86],'hasil TF-IDF D25':row[87],'hasil TF-IDF D26':row[88],'hasil TF-IDF D27':row[89],'hasil TF-IDF D28':row[90],'hasil TF-IDF D29':row[91],'hasil TF-IDF D30':row[92]})
        csvfile.close() 

# Menggabungkan seluruh hasil pembobotan ke dalam 1 buah list
def gabungHasil(terms,tf):
    hasil=[]
    a=0
    for word in terms:
        hasil.append([])
        hasil[a].append(word)
        for row in tf[a]:
            hasil[a].append(row)
#        for row in ltf[a]:
#            hasil[a].append(row)
#        hasil[a].append(df[a])
#        hasil[a].append(idf[a])
#        for row in tfidf[a]:
#            hasil[a].append(row)
        a+=1
    return hasil
        
# Main method
def RUN():
    terms=term('hasilPreProcessingBaru.csv')
    prepro=getPreprocessing('hasilPreProcessingBaru.csv')
    hasilTF = rawTF(terms,prepro)
#    hasilLTF= logTF(hasilTF)
#    hasilDF = docFreq(hasilTF)
#    hasilIDF = inverseDF(hasilDF,30)
#    hasilTFIDF = tfidf(hasilTF,hasilIDF)
    hasilGabungan=gabungHasil(terms,hasilTF)
#    writehasilexcel(hasilGabungan)
#    writehasilcsv(hasilGabungan)
    return hasilGabungan
    
        