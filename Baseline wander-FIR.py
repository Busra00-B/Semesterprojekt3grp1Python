#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:13:28 2022

@author: BILGIN
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import wfdb

# Read the two ECG signals (raw, filtered) and read 
# the related information.
signals, info = wfdb.rdsamp('rec_2', channels=[0, 1], 
                              sampfrom=0, sampto=2000)

Fs=500
Ts=1/Fs


t=np.arange(0,2000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]



#design af FIR-filter-baseline wander støj

#L skal være over 1000 det står i artiklen
L=303

#Fc er cutt-off frekvensen som er angivet i artiklen
Fc=0.667

#designet filter
FiltHP = signal.firwin(numtaps=L, cutoff=0.667, fs=1/Ts, pass_zero=False)
                      



#FiltU=den graf hvor vi har filteret støjen fra rådata(,x) hvor x er den signal vi vil filtrere
FiltUB=signal.filtfilt(FiltHP,1,ecg0)
plt.title(" EKG filtret for baseline")
plt.xlabel("tids")
plt.ylabel("milivolts")
plt.plot(t,FiltUB)
plt.show()

#frekvensdomænet-plotte filtrede ekg 
plt.magnitude_spectrum(FiltUB,Fs)
plt.title("Uden baseline wander støj")
plt.xlabel("frekvensdomænet")
plt.show()
