# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:19:25 2022

@author: 181805049-181805061
"""
import matplotlib.pyplot as plt
from scipy.io import loadmat
import sys
from scipy import signal
import numpy as np
fs =1
winsize = fs * 5
winhop = fs
amp = 2 * np.sqrt(2)
i = 0


s1b = loadmat(r"C:\Users\umuts\Desktop\dataverse_files\data\0009_8min.mat")
s1w = loadmat(r"C:\Users\umuts\Desktop\dataverse_files\data\mat\0015_8min.mat")




s1w_eeg_channel_label=s1w["data"]["channel_labels"][0,0][0,0]
# EEG signal for channel 0 to 4 
s1w_eeg_ch0=s1w["data"]["EEG"][0,0][0:,0]
s1w_eeg_ch1=s1w["data"]["EEG"][0,0][0:,1]
s1w_eeg_ch2=s1w["data"]["EEG"][0,0][0:,2]
s1w_eeg_ch3=s1w["data"]["EEG"][0,0][0:,3]

# EOG signal for channel 0 1 2 
s1w_eog_ch0=s1w["data"]["EOG"][0,0][0:,0]
s1w_eog_ch1=s1w["data"]["EOG"][0,0][0:,1]
s1w_eog_ch2=s1w["data"]["EOG"][0,0][0:,2]




def on_press(event):
    global i
    print('press', event.key)
    sys.stdout.flush()
    
    lower = i
    upper = i + winsize
    
   

    ax4.cla()
    ax4.plot(s1w_eeg_ch0[lower:upper], alpha=0.8, label="ch0")
    ax4.plot(s1w_eeg_ch1[lower:upper], alpha=0.8,label="ch1")
    ax4.plot(s1w_eeg_ch2[lower:upper], alpha=0.8, label="ch2")
    ax4.plot(s1w_eeg_ch3[lower:upper], alpha=0.8,label="ch3")
    ax4.legend( loc='upper right', shadow=True)
    
    
    ax5.cla()
    ax5.plot(s1w_eog_ch0[lower:upper], alpha=0.8, label="ch0")
    ax5.plot(s1w_eog_ch1[lower:upper], alpha=0.8,label="ch1")
    ax5.plot(s1w_eog_ch2[lower:upper], alpha=0.8, label="ch2")
    ax5.legend( loc='upper right', shadow=True)
    
    
    if event.key == 'right':
        i = i + winhop
        fig.canvas.draw()
    elif event.key == 'left':
        i = i - winhop
        fig.canvas.draw()

fig = plt.figure()

fs = 10e3
amp = 2 * np.sqrt(2)

ax0=fig.add_subplot(321)
f, t, Zxx = signal.stft(s1w_eeg_ch0, fs, nperseg=1000)
ax0.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp, shading='gouraud')


ax1=fig.add_subplot(322)
f, t, Zxx = signal.stft(s1w_eog_ch0, fs, nperseg=1000)
ax1.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp, shading='gouraud')






ax2=fig.add_subplot(323)
ax2.plot(s1w_eeg_ch0, alpha=0.8, label="ch0")
ax2.plot(s1w_eeg_ch1, alpha=0.8,label="ch1")
ax2.plot(s1w_eeg_ch2, alpha=0.8, label="ch2")
ax2.plot(s1w_eeg_ch3, alpha=0.8,label="ch3")
ax2.legend( loc='upper right', shadow=True)


ax3 = fig.add_subplot(324)
ax3.plot(s1w_eog_ch0, alpha=0.8, label="ch0")
ax3.plot(s1w_eog_ch1, alpha=0.8,label="ch1")
ax3.plot(s1w_eog_ch2, alpha=0.8, label="ch2")
ax3.legend( loc='upper right', shadow=True)




ax4 = fig.add_subplot(325)
ax4.grid()

ax5 = fig.add_subplot(326)
ax5.grid()



fig.canvas.mpl_connect('key_press_event', on_press)

plt.show()


s1w_eeg_trig=s1w["data"]["trigger"][0,0][0:,0]
s1w_eeg_head=s1w["data"]["header"][0,0][0:,0]
s1w_eeg_FIR_resample=s1w["data"]["FIR_resample"][0,0][0]
s1w_eeg_subjective_report=s1w["data"]["subjective_report"][0,0]