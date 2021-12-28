# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:04:42 2021

nama :sarah sakinah
nim :065002100033
prodi:sistem informasi
"""
print("@@@@  @@@  @@@@  @@@  @   @")
print("@     @ @  @  @  @ @  @   @")
print("@@@@  @@@  @@@@  @@@  @@@@@")
print("   @  @ @  @@    @ @  @   @")
print("   @  @ @  @ @   @ @  @   @")
print("@@@@  @ @  @  @  @ @  @   @")
def selection():
    list=[]
    askfor=int(input('masukkan jumblah angka pada list: '))
    for i in range(askfor):
        i+=1
        list.append(int(input(f'Masukan angka ke {i}: ')))
    print (f'list angka -> {list}')
    for i in range(0,len(list)-1):
        p=0
        mini=list[-1]
        for j in range(i,len(list)):
            if list[j]<=mini:
                mini=list[j]
                p=j
        list[i],list[p]=list[p],list[i]
    print(f'list dengan selection sort: {list}')
selection()