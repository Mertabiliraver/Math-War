import time
import random
i=0
süre=0
puan=0
print("""
*********************************
Çarpım tablosu ezberleten program
Her doğru cevap +5 PUAN
Her yanlış cevap -5 PUAN

Başarılar...
*********************************
""")
x=time.sleep(4)

while True:
    x=random.randint(0,10)
    y=random.randint(0,10)
    int(x)
    int(y)
    print("\nSence cevap kaçtır ?\n",x,"x",y)
    cevap=int(input("Cevap :"))


    
    if (cevap==x*y):
        print("\nDoğru cevap ! (+5 Puan)")
        puan+=5
        time.sleep(1)
        print("\nPuanın:",puan)
        continue
    
    elif x==30:
         print("Süre doldu !\nToplam puan :",puan)
         break
    else:
        print("\nÜzgünüm yanlış cevap (-5 Puan)")
        puan-=5
        time.sleep(1)
        print("\nPuanın:",puan)
        continue

