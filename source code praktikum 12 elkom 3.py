# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:03:41 2021

nama :sarahsakinah
prodi:sistem informasi
nim :065002100033
"""
print("@@@@  @@@  @@@@  @@@  @   @")
print("@     @ @  @  @  @ @  @   @")
print("@@@@  @@@  @@@@  @@@  @@@@@")
print("   @  @ @  @@    @ @  @   @")
print("   @  @ @  @ @   @ @  @   @")
print("@@@@  @ @  @  @  @ @  @   @")

def bubble_sorted():
    list=[]
    askfor =int(input('masukkan jumblah angka pada list: '))
    for i in range(askfor):
        i+=1
        list.append(int(input(f'masukan angka ke {i}:')))
    print('list angka -> ',list)
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(f'Hasil Bubble Sort = {list}')
bubble_sorted()