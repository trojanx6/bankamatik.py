sys import çıkışından

rastgele içe aktar

# şimdi ilk önce kullanıcıdan limit bilgisi.

limit = int(input("ATM limitiniz: "))

hesapa= input("kullanıcı Adı giriniz: ")

hesappwd = input("kullanıcı Sifresi: ")

heno = rastgele.randint(11111,999999)

mai = input("mail adresinizi giriniz: ")

print(f"hesap nonuz: {heno}")

#Buburda dursun foksiyon ile işlemler yapıcaz

Yazdır("""

casus banka

casus banka (•)

==> para çek 1

==> 2 para yatırır

==> hesap bilgisi 3

""")

islem = int(input("islem seçiminiz: "))

# Simdi foksiyonları oluşturalım global ile limiti alıcaz.

def pa_c():

    küresel sınır

    # global ild limiti foksiyonu local alandada kullanına

    us = input("Hesap adı: ")

    pwd = input("Hesap şifresi: ")

    # Hesap adı şifresi alındı

    if (us == hesapa) ve (pwd == hesappwd):

        #hesap adi sifresi dogru ise alltaki kod blogu çalisacak

        çek = int(input("Çekilecek tutar: "))

        #cekilmek istenilen tutar soruluyor

        print(f"Bu kadar para çekiliyor...{cek}")    

        limit -= çek

        print(f"kalan bakiyeniz: {limit}")

        #kalan bakiyeyi soyledik           

    Başka:

        print("Yanlış tekrar deneyiniz!!!!")

        # eğef bilgiler yanlış ise buraya gelicek python ve

        sistem.çıkış()

        #çıkış progami bittirecek

        

tanım pa_y():

    küresel sınır

    us = input("Kullanıcı isim: ")

    pwd = input("Kullanıcı şifresi: ")

    bize == hesapa ve pwd == hesappwd ise:

        yatir = int(input("yatırılacak: "))

        limit += yatir

        #limitin uzerine ekliyoruz

        print(f"şuanki bakiye {limit}")

        #toplkam tutari soyuyoruz

        

    Başka:

        print("yanlış!!")

        sistem.çıkış()

        #yanlis bilgiler ise progam bitiyor

    

islem == 1:

    pa_c()

elif islem == 2:

    pa_y()
