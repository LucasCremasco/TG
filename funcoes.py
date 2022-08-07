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