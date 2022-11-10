# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:05:44 2022

@author: Hawa Aprilia Utami
"""

def cek(bilangan):
    for i in range(2, bilangan):
        if (bilangan % i) == 0:
            return f"{bilangan} bukan bilangan prima karena habis dibagi oleh {i}"
    else:
        return f"{bilangan} adalah bilangan prima"

def validasi(angka):
    if angka > 1:
        return cek(angka)
    else:
        return f"{angka} bukan bilangan prima"


try:
    angka = int(input("Masukkan angka: "))
    print(validasi(angka))
except ValueError:
    print("Input harus berupa bilangan bulat")