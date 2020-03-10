#!/usr/bin/env python
'''
Example of (almost) all widgets, that you can use in PySimpleGUI.
'''

import PySimpleGUI as sg
import os
import random
import subprocess


def neu(modus):
    if modus == 1:
        ba = random.choice(mypics)
        be = random.choice(mypics)
        bi = random.choice(mypics)
        bo = random.choice(mypics)
        bu = random.choice((bi, ba, be, bo))
        window["bild1"].update(image_filename=ba+".png")
        #window["text1"].update(bi)
        window["bild2"].update(image_filename=be+".png")
        #window["text2"].update(bo)
        window["bild3"].update(image_filename=bi+".png")
        #window["text3"].update(ba)
        window["bild4"].update(image_filename=bo+".png")
        #window["text4"].update(be)
        window["big"].update("Klicke auf {}".format(bu))
        window["progressbar"].UpdateBar(punkte)
        return ba, be, bi, bo, bu
    
    elif modus == 2:
        ba = random.choice(mypics)
        window["bild1"].update(image_filename=ba+".png")
        window["bild2"].update(image_filename=ba+".png")
        window["bild3"].update(image_filename=ba+".png")
        window["bild4"].update(image_filename=ba+".png")
        window["big"].update("Was ist auf dem Bild?")
        window["progressbar"].UpdateBar(punkte)
        return ba

mypics = []
for root, dirs, files in os.walk("."):
    print(files)
    for f in files:
        if f[-4:] == ".png":
            mypics.append(f[:-4])
print("meine bilder:")
print(mypics)           
punkte = 0
total= 0
layout = [
    
    [sg.Text('Vokabeltrainer! Click the clock', key="big", size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE), sg.Button(key="speak again")],
    [sg.Text("punkte: {}".format(punkte), key="punkte", size=(15, 1), font=("Helvetica", 25)), 
     sg.ProgressBar(20, orientation='h', size=(20, 20), key='progressbar'), sg.Cancel()],
    [sg.Text("total: {}".format(punkte), key="total", size=(15, 1), font=("Helvetica", 25)), 
     sg.ProgressBar(20, orientation='h', size=(20, 20), key='time')],
    #[sg.Text('.    ', key="text1"), sg.Text('.    ', key="text2"), sg.Text('.   ', key="text3"),sg.Text('.    ', key="text4")],
    [sg.Output(size=(80, 5))],
   # [sg.Text("punkte: {}".format(punkte), key="punkte")],
    [sg.Button(key="bild1", button_color=sg.TRANSPARENT_BUTTON, image_filename="clock.png"), sg.Button(key="bild2", button_color=sg.TRANSPARENT_BUTTON, image_filename="road.png")],
    [sg.Button(key="bild3", button_color=sg.TRANSPARENT_BUTTON, image_filename="clock.png"), sg.Button(key="bild4", button_color=sg.TRANSPARENT_BUTTON, image_filename="road.png")],
    
    [sg.Text("Wort eintippen und Enter drücken: >>>", key="i1"), 
     sg.InputText('', key="i2"), 
     sg.Button("Enter", key="enter", bind_return_key=True)
    ]]
   #  sg.Text("punkte: {}".format(punkte), key="punkte")],
    #[sg.Button("ok"), sg.Button("next"), sg.Button("random"), sg.Cancel()]]

#bi, bo, be, ba, bu = neu()
window = sg.Window('Everything bagel', layout)
#window = sg.Window('Custom Progress Meter', layout)
#progress_bar = window['progressbar']
window.finalize()
ba, be, bi, bo, bu = neu(1)
window.finalize()
gamemode=1

while True:
    event, values = window.read()
    if event in (None, "Cancel"):
        break
    #print(values)
       
    if event== "speak again":
        subprocess.call(("espeak", bu if gamemode == 1 else ba))
        continue
    if gamemode==1:    
        if event== "bild1":
            #print("ba und bu:",  ba,  bu)
            if ba == bu:
                print ("correct")
                punkte=punkte+1
                total=total+1
            else:
                print ("Ohh, no! This was a", ba)
                punkte=punkte-1
                total=total-1 
                
        if event== "bild2":
            if be == bu:
                print ("nice")
                punkte=punkte+1
                total+=1  #+=1
            else:
                print ("Ohh, no! This was a", be)
                punkte=punkte-1
                total-=1  #-=1

        if event== "bild3":
            if bi == bu:
                print ("super")
                punkte=punkte+1
                total+=1
            else:
                print ("Ohh, no! This was a", bi)
                punkte=punkte-1
                total-=1 
        
        if event== "bild4":
            if bo == bu:
                print ("very good")
                punkte=punkte+1
                total+=1
            else:
                print ("Ohh no! This was a", bo)
                punkte=punkte-1
                total-=1 
                
    if event=="enter":
        print(values["i2"])
        if gamemode == 2:
            if values["i2"].lower()==ba:
                print ("Bravo, gut gemacht")
                punkte+=1
                total+=1
            else:
                print ("Falsch,", ba)
                punkte-=1
                total-=1
            values["i2"] = ""  
            window["i2"].update("")    
    #----------------------        
    window["punkte"].update("punkte: {}".format(punkte))
    window["progressbar"].UpdateBar(punkte)
    window["total"].update("total: {}".format(total))
    if punkte==20 and gamemode==1:
        gamemode+=1
        punkte = 0
        
        window["bild1"].update(visible=True)
        window["bild2"].update(visible=True)
        window["bild3"].update(visible=True)
        window["bild4"].update(visible=True)
        
        window.finalize()
    if punkte==20 and gamemode==2:
        gamemode=1
        punkte=0
         
        window["bild1"].update(visible=True)
        window["bild2"].update(visible=True)
        window["bild3"].update(visible=True)
        window["bild4"].update(visible=True)
        window.finalize()
        
        
    if gamemode==1:
        ba, be, bi, bo, bu = neu(1)
    elif gamemode==2:
        ba = neu(2)
    
    
print("bye")
