from gtts import gTTS
import gtts
import os
import time
import csv
l=['whore bag']
a=gtts.lang.tts_langs()
f=open('log.csv','a')

for i in range(len(l)):
    os.mkdir(l[i])
    time.sleep(2)
    print("Sleep")
    for j in a:
        tts = gTTS(l[i],lang=j)
        s = l[i]+'/'+l[i]+'_'+ j +'.mp3'
        tts.save(s)
        print(s)
        f.write(s)
        time.sleep(0.75)
       
    #print("ERROR")
f.close()

       
