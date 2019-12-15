#Amelia Kosasih - 175150200111027
#Anugrah Prasetia - 175150200111004
#Griselda Anjeli Sirait - 175150200111002

from sklearn.metrics import confusion_matrix

def ConfusionMatrix(true,pred):
    return confusion_matrix(true, pred, labels=["Positif", "Negatif"])
    
def countAccuracy(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    c = confusionMtx[1][0]
    d = confusionMtx[1][1]
    accuracy = (a+d)/(a+b+c+d)
    return accuracy 

def countRecallPositif(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    c = confusionMtx[1][0]
    d = confusionMtx[1][1]
    recallPositif = a/(a+c)
    return recallPositif

def countRecallNegatif(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    c = confusionMtx[1][0]
    d = confusionMtx[1][1]
    recallNegatif = d/(b+d)
    return recallNegatif 

def countPrecisionPositif(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    c = confusionMtx[1][0]
    d = confusionMtx[1][1]
    precisionPositif = a/(a+b)
    return precisionPositif

def countPrecisionNegatif(confusionMtx):
    a = confusionMtx[0][0]
    b = confusionMtx[0][1]
    c = confusionMtx[1][0]
    d = confusionMtx[1][1]
    precisionPositif = d/(c+d)
    return precisionPositif
