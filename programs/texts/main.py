import pandas as pd
import numpy as np
import scipy.spatial as spsp
import re

file_obj = open('sentences.txt', 'r')
k = 0
sentence_count = 0
unique_index = 0
dict = {}

for line in file_obj:
    str = line.strip()
    str = str.lower()
    arr = re.split('[^a-z]', str)
    for i in range(len(arr)):
        if (arr[i] == '') == False :
            if (arr[i] in dict) == False:
                dict[arr[i]] = unique_index
                unique_index += 1
    sentence_count += 1
matrix = np.zeros((sentence_count, len(dict)))
sentence_count = 0

file_obj = open('sentences.txt', 'r')
for line in file_obj:
    str = line.strip()
    str = str.lower()
    arr = re.split('[^a-z]', str)
    for i in range(len(arr)):
         if (arr[i] == '') == False:
            if arr[i] in dict:
                matrix[sentence_count][dict[arr[i]]] += 1
    sentence_count += 1
answers_arr = []
for i in range(1, sentence_count):
    answers_arr.append([spsp.distance.cosine(matrix[0], matrix[i]), i])
print(len(answers_arr))
answers_arr.sort()
print(answers_arr[0], answers_arr[1], answers_arr[2])