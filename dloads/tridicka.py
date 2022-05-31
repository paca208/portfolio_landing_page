import shutil
import os
import sys
import re
import ctypes
import easygui

path = easygui.enterbox("Kde mám čistit?", "Zadej misto",sys.path[0])
list = os.listdir(path)
seznam_pouzitych = ""

for file in list:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == 'docx':
        jmeno_slozky = 'Word Dokumenty'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka
        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    
    if ext == 'txt':
        jmeno_slozky = 'Poznamky txt'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka
        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    
    if ext == 'png':
        jmeno_slozky = 'Random Obrazky'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka
        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    
    if ext == 'jpg':
        jmeno_slozky = 'Random Obrazky'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka

        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    if ext == 'gif':
        jmeno_slozky = 'Random Obrazky'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka

        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    if ext == 'pdf':
        jmeno_slozky = 'PDF Dokumenty'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"    
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka

        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    
    if ext == 'url':
        jmeno_slozky = 'Steam a Epic Hry'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"
        searchRL = re.search('Rocket League', name)
        if searchRL:
            continue
        else:
            if os.path.exists(path+'/'+jmeno_slozky):
                shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
                seznam_pouzitych += polozka

            else:
                os.makedirs(path+'/'+jmeno_slozky)
                shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    if ext == 'pptx':
        jmeno_slozky = 'Prezentace'
        polozka = name + "." + ext + " do" + " " + jmeno_slozky + "\n"    
        if os.path.exists(path+'/'+jmeno_slozky):
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
            seznam_pouzitych += polozka

        else:
            os.makedirs(path+'/'+jmeno_slozky)
            shutil.move(path+'/'+file, path+'/'+jmeno_slozky+'/'+file)
    
if not seznam_pouzitych:
    ctypes.windll.user32.MessageBoxW(0, "Nebylo co vytridit :(", "Je tu cisto", 1)

else:
    ctypes.windll.user32.MessageBoxW(0, seznam_pouzitych, "Vytrideno:", 1)