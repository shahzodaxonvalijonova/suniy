# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LoXvRCbSHBBPLeiIWvQ6eogLRiTq8qST
"""

import numpy as np
array_1d = np.array([1,2,3,4,5])
array_2d = np.array([[1,2,3], [4,5,6]])
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
product_array = np.prod(array_1d)

print("1D Massiv: ", array_1d)
print("2D Massiv:\n", array_2d)
print("Massivlar yig'indisi: ", sum_array)
print("O'rtacha: ", mean_array)
print("Ko'paytma: ", product_array)

import pandas as pd


data = {
    'ism': ['Shahzoda', 'Vali', 'Sardor', 'Xurshida', 'Mohchehra', 'Maftuna', 'Aziza', 'Mahmuda', 'Farangis', 'Alisher'],
    'Yoshi': [25, 30, 22, 18, 19, 20, 21, 23, 24, 28],
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro', 'Surxandaryo', 'Fargona', 'Andijon', 'Namangan', 'Fargona', 'Jizzax', 'Toshkent']
}

df = pd.DataFrame(data)


print(df)


young_people = df[df['Yoshi'] < 20]
print("20 yoshdan kichiklar:\n", young_people)


df['Yoshi'] += 1
print("Yangilangan DataFrame:\n", df)


fargona_people = df[df['Shahar'] == 'Fargona']
print("Fargonada yashaydiganlar:\n", fargona_people)