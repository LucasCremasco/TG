import pandas as pd
import numpy as np
import os



def path_arquivos(path):
    path_n1 = path
    files_n1 = os.listdir(path_n1)
    path_imagens = dict()
    img_0 = []

    for arq1 in files_n1:
        path_n2 = path_n1 + '\\' + arq1
        files_n2 = os.listdir(path_n2)
        
        path_n3 = path_n2  + '\\' + files_n2[0]
        files_n3 = os.listdir(path_n3)

        path_n4 = path_n3  + '\\' + files_n3[0]
        files_n4 = os.listdir(path_n4);

        path_n5 = [path_n4  + '\\' + arquivo for arquivo in files_n4]
        path_imagens[f'{arq1}'] = path_n5

        img_0.append(path_n5[0])
    return path_imagens, img_0



def somatorio_dimensao(img, seleciona = 'coluna'):
    somatorio = []

    if seleciona == 'coluna':

        for coluna in range(y):
            soma = np.sum(img[:,coluna])
            somatorio.append(soma)
        return somatorio
        
    else:
        for linha in range(x):
            soma = np.sum(img[linha,:])
            somatorio.append(soma)
        return somatorio

def seleciona_perna(somatorio):
    maximo = np.where(np.max(somatorio) == somatorio)[0][0]
    somatorio2 = somatorio.copy()
    
    while maximo < y / 2:
        somatorio2[maximo] = -99999
        maximo = np.where(np.max(somatorio) == somatorio)[0][0]

    interval = maximo - 150;
    minimo = np.where(np.min(somatorio[interval:maximo]) == somatorio)[0][0]


#    minimo_dir = np.where(np.max(somatorio[minimo] - somatorio[maximo:]))[0][0]

    return minimo