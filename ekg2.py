#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:34:18 2022

@author: BILGIN
"""

#få EKG data ud fra zipfilen. 

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import wfdb
import requests
import json

# Read the two ECG signals (raw, filtered) and read 
# the related information.
signals, info = wfdb.rdsamp('rec_2', channels=[0, 1], 
                              sampfrom=0, sampto=1000)

Fs=500
Ts=1/Fs


t=np.arange(0,1000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]

#tidsdomænet
#ekg med støj ecg0
plt.title('Rå EKG data')
plt.xlabel('tid(s)')
plt.ylabel('milivolts')
plt.plot(t,ecg0)
plt.show()

#ekg uden støj ecg1
#plt.title('Rå EKG data uden støj')
plt.xlabel('tid(s)')
plt.ylabel('milivolts')
plt.plot(t,ecg1)
plt.show()

#frekvensdomænet
plt.title("Rå EKG data")
#plot med støj, den blå peak omkring 50 hz skal filtreres fra med vores designede filter. 
plt.magnitude_spectrum(ecg0,Fs,color="red")

#plt.title('Rå EKG data uden støj')

#plot uden støj, og her kan vi se at den peak omkring 50 hz er væk

#plt.magnitude_spectrum(ecg1,Fs,color="blue")


#sende data til backenden
#bs står for ekg data som er konverteret til string fra arrayliste
#kilde https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
#giv et andet navn end bs og husk det er data med støj du har sendt, det skal nok være data uden støj du skal sende
#bs=str(" ,".join(ecg0))

#https://www.codegrepper.com/code-examples/python/TypeError%3A+sequence+item+0%3A+expected+str+instance%2C+float+found+numpy kilde til det nedentsående
#ekg = ','.join([str(ecg0) for i in ecg0])
#ekg1 = ','.join(map(str, ecg0))
#ekg2=",".join([str(ecg0) for ecg0 in ecg0])
#vi bruger ikke det somstår ovenover

#r kan laves om
r =requests.post('http://localhost:8080/EKGJournalSystem_war/rest/ecg', json={"data":ecg1.tolist()})











