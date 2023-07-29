#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zaafiyet Analizi")
print("code by @blody")
print("""
Zaafiyet Analizi Programına Hoş Geldiniz.
""")

hedefip = input("Hedef İp Girin: ")

os.system("nikto -h " + hedefip)
