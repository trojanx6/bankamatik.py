from sys import exit

import random

# şimdi ilk önce kullanıcıdan limit bilgisi alalım.

limit = int(input("ATM limitiniz: "))

hesapa= input("kullanıcı Adı giriniz: ")

hesappwd = input("kullanici Sifresi: ")

heno  = random.randint(11111,999999)

mai = input("mail adresiniz giriniz: ")

print(f"hesap nonuz: {heno}")

# Bu burda dursun foksiyon ile işlemleri yapıcaz

print("""

spy banka 

casus banka (•)

==> para çek 1

==> para yatır 2

==> hesap bilgisi 3

""")

islem = int(input("islem seciniz: "))

# Simdi foksiyonları oluşturalım global ile limiti alıcaz.

def pa_c():

    global limit

    # global ild limiti foksiyonu local alandada kullana biliyoruz

    us = input("Hesap adı: ")

    pwd = input("Hesap şifresi: ")

    # Hesap adı şifresi aldık

    if (us == hesapa) and (pwd == hesappwd):

        #hesap adi sifresi dogru ise alltaki kod blogu çalisacak

        cek = int(input("Çekilecek tutar: "))

        #cekilmek istenilen tutar soruluyor

        print(f"Bu kadar para çekiliyor...{cek}")    

        limit -= cek

        #kalan bakiyeyi soyledik           

    else:

        print("Yanlış oturum Tekrar deneyiniz!!!!")

        # eğef bilgiler yanliş ise buraya gelicek python ve 

        sys.exit()

        # exit yapip progami bittirecek

        

def pa_y():

    global limit 

    us = input("Kullanıcı isim: ")

    pwd = input("Kullanıcı şifresi: ")

    if us == hesapa and pwd == hesappwd:

        yatir = int(input("yatırılacak tutar: "))

        limit += yatir

        # limitin ûzerine ekliyoruz

        print(f"şuanki bakiye {limit}")

        #toplfam tutari soyliyoruz

        

    else:

        print("yanliş oturum!!")

        sys.exit()

        #yanlis bilgiler ise progam bitiyor

    

if islem == 1:

    pa_c()

elif islem == 2:

   
