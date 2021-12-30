import re
import hashlib
from hashlib import blake2b
from hashlib import shake_256
from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD160
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA3_224
from attr import has
from Crypto.Cipher import DES
import base32hex
from secrets import token_bytes
from Crypto.Cipher import AES

import pypyodbc




class dilKontrol():

    def _init_(self, text):
        self.text = text

    def Cumlelere_ayir(self):
        count = 0
        count2 = 0
        count3 = 0
        i = self.text
        cumle = i.split(".")
        cumle2 = i.split("?")
        cumle3 = i.split("!")

        try:
            if (len(cumle) != 0):
                count = len(cumle) - 1
                if (len(cumle2) != 0):
                    count2 = (len(cumle2) - 1)
                    if (len(cumle3) != 0):
                        count3 = (len(cumle3) - 1)

            elif (len(cumle2) != 0):
                count = len(cumle2)
                if (len(cumle3) != 0):
                    count3 = (len(cumle3) - 1)

        except(ValueError):
            print(ValueError)

        else:
            print("Cümle Yok")

        return count + count2 + count3




    def Kelimelere_Ayir(self):
        x = self.text.split()
        non_kelime = list("!?.-*/")

        for i in non_kelime:
            for j in x:
                if j == i:
                    x.remove(j)

        return len(x)

    def Kac_adet_SesliHarf(self):
        count = 0
        i = self.text
        sesli_harf = 'AEIİOÖUÜaeıioöuü'
        for x in i:
            if x in sesli_harf:
                count += 1
        return count

    def Buyuk_Unlu_Uyumu(self):
        kalin_unluler = list("aıou")
        ince_unluler = list("eiöü")
        count = 0
        x = self.text.split()
        print(x)

        for i in x:
            kelime = i
            if (sum(kelime.count(i) for i in kalin_unluler)) != 0 and (
            sum(kelime.count(j) for j in ince_unluler)) != 0:
                pass

            else:
                count = count + 1
        return count, (len(x) - count)

    def Buyukharf_Bul(self):
        i = self.text
        count = 0
        countk = 0
        cumle = i.split(". ")
        cumle2 = i.split("?")
        cumle3 = i.split("!")
        buyuk = False
        buyuk2 = False
        buyuk3 = False
        if len(cumle) >= 2:
            for cumleler in cumle:
                for kelime in cumleler:
                    if kelime.istitle():
                        count = count + 1
                        buyuk = True
                        break
                    else:
                        countk = countk + 1
                        break
        if len(cumle2) >= 2:

            for cumleler2 in cumle2:
                for kelime in cumleler2:
                    if kelime.istitle():
                        count = count + 1
                        buyuk2 = True
                        break
                    else:
                        countk = countk + 1
                        break
        if len(cumle3) >= 2:
            for cumleler3 in cumle3:
                for kelime in cumleler3:
                    if kelime.istitle():
                        count = count + 1
                        buyuk3 = True
                        break
                    else:
                        countk = countk + 1
                        break
        if buyuk == True and buyuk2 == True and buyuk3 == True:
            count = count - 2
        elif buyuk == True and buyuk2 == True or buyuk == True and buyuk3 == True or buyuk2 == True and buyuk3 == True:
            count = count - 1

        return count, countk

    def En_Uzun_Kelimeyi_bul(self):
        text = self.text
        kelimeler = text.split()
        uzunluklar=[]

        for i in kelimeler:
            uzunluklar.append(len(i))

        en_uzun = max(uzunluklar)
        sirasi = uzunluklar.index(en_uzun)
        en_uzun_kelime = kelimeler[sirasi]

        return en_uzun_kelime


class sifrelemeYontemleri():
    def _init_(self, girdi):

        self.girdi = girdi

    def MD5_Sifrele(self):
        d = hashlib.md5()
        d.update(self.girdi.encode('utf-8'))
        return d.hexdigest()

    def SHA256_Sifrele(self):
        hashObject = SHA256.new()
        hashObject.update(self.girdi.encode('utf-8'))



        return hashObject.hexdigest()

    def Blake2_sifrele(self):
        hashObject = blake2b()
        hashObject.update(self.girdi.encode('utf-8'))

        return hashObject.hexdigest()

    def Whirl_Pool(self):
        hashobject = hashlib.new('whirlpool')
        hashobject.update(self.girdi.encode('utf-8'))

        return hashobject.hexdigest()

    def RIPEMD160_Sifrele(self):
        hashobject = RIPEMD160.new()
        hashobject.update(self.girdi.encode('utf-8'))

        return hashobject.hexdigest()

    def SHA3_224_Sifrele(self):
        hashobject = SHA3_224.new()
        hashobject.update(self.girdi.encode('utf-8'))
        return hashobject.hexdigest()

    def DES_Sifrele(self, key):  # 8byte girilecektir Data Encryption Standart
        try:
            msg = self.girdi
            cipher = DES.new(key, DES.MODE_EAX)
            nonce = cipher.nonce
            ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))

            return ciphertext
        except(ValueError, IOError):
            print(ValueError, IOError)

    def AES_Sifreleme(self, key):  # 16 byte anahtar girilecektir Advanced Encrption Standart
        try:
            msg = self.girdi
            cipher = AES.new(key, AES.MODE_EAX)
            nonce = cipher.nonce

            ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
            return ciphertext

        except(ValueError, IOError):
            print(ValueError, IOError)



class veriTabani():


    def _init_(self,veri):
        self.veri = veri



    def Yaz(self,data):
        x = self.veri

        try:
            db = pypyodbc.connect(
                'Driver={SQL Server};'
                'Server=APOKSK1;'
                'Database=Python;'
                'Trusted_Connection=True;'
            )
            imlec = db.cursor()

            komut = 'INSERT INTO Python_yazdir Values (?,?,?,?)'
            veriler = data
            sonuc = imlec.execute(komut,veriler)
            db.commit()

        except(ValueError):
            print("4 tane deger giriniz")
            print(ValueError)


    def Cek (self):
        db = pypyodbc.connect(
            'Driver={SQL Server};'
            'Server=APOKSK1;'
            'Database=Python;'
            'Trusted_Connection=True;'
        )
        imlec = db.cursor()

        imlec.execute('Select * From Python_yazdir')

        kullanicilar = imlec.fetchall()

        for i in kullanicilar:
            print(i)


            return kullanicilar



class Help():
    def bilgiGoster(self):

        print("Modulde toplam 3 class vardır.\n1.class dilKontrol\n2.class sifrelemeYontemleri\n3.class Veri_Tabani"
            "\n--->dilKontrol sınıfının init fonksiyonu ilk başta string bir parametre alır ve işlemlerini ona göre yapar"
            "\n--->dilKontrol sinifinin fonksiyonlari:"
            "\n _init_ : parametre alır ve kayit eder"
            "\nCumlelere_ayir: init fonksiyonundan aldigi string ifadeyi Cumlelerine ayirir ve geri dondurur"
            "\nKelimelere_ayir : init fonksiyonundan aldigi string ifadeyi kelimelerine ayirir ve geri dondurur"
            "\nKac_Adet_SesliHarf : init fonksiyonundan aldigi string ifadede kac adet sesli harf oldugunu bulur ve geri dondurur"
            "\nBuyuk_Unlu_Uyumu : init fonksiyonundan aldigi string ifadede buyuk unlu uyumuna uyup uymayanları bulur ve geri dondurur"
            "\nBuyukharf_Bul : init fonksiyonundan aldigi string ifadede ki cumlelerin buyuk harfle mi basliyor onu bulur ve geri dondurur"
            "\nEn__Uzun_Kelimeyi_bul : init fonksiyonundan aldigi string ifadede ki en uzun kelimeyi bulur ve geri dondurur"
            "\n\n--->sifrelemeYontemleri sınıfının init fonksiyonu ilk basta string bir parametre alir"
            "\n--->sifrelemeYontemleri sinifinin fonksiyonlari:"
            "\n _init_ : parametre alır ve kayit eder"
            "\nMD5_Sifrele : init fonksiyonundan aldigi parametreyi md5 algoritmasıyla sifreler ve geri dondurur"
            "\nSHA256_Sifrele : init fonksiyonundan aldigi parametreyi SHA256 algoritmasıyla sifreler ve geri dondurur"
            "\nBlake2_sifrele : init fonksiyonundan aldigi parametreyi Blake2 algoritmasıyla sifreler ve geri dondurur"
            "\nWhirl_Pool : init fonksiyonundan aldigi parametreyi Whirl Pool algoritmasıyla sifreler ve geri dondurur"
            "\nRIPEMD160_Sifrele : init fonksiyonundan aldigi parametreyi RIPEMD160 algoritmasıyla sifreler ve geri dondurur"
            "\nSHA_224_Sifrele : init fonksiyonundan aldigi parametreyi SHA3_224 algoritmasıyla sifreler ve geri dondurur"
            "\nDES_Sifrele : init fonksiyonundan bir parametre alir kendiside byte tipinde 8byte bir parametre alir aldigi parametrleri DES algoritmasi ile sifreler ve geri dondurur"
            "\nAES_Sifrele : init fonksiyonundan bir parametre alir kendiside byte tipinde 16byte bir parametre alir aldigi parametrleri AES algoritmasi ile sifreler ve geri dondurur"
            "\n\n--->veriTabani sinifinin init fonksiyonu ilk basta string bir deger alıp kayit eder"
            "\n--->veriTabani sinifinin fonksiyonlari :"
            "--init-- : strin bir parametre alir ve kayıt eder"
            "\nYaz : 4 elemanli bir tuple parametresi alir ve veri tabanina yazar"
            "\nCek : parametre almaz veri tabanından verileri ceker ve geri dondurur")

    text = str(input("Lütfen Bir Metin Giriniz: "))
   
    islem = input("Lütfen Kontrol Edilecek Fonksiyonu Giriniz: ")

    dilkontrol = dilKontrol(text5
    sifreleme = sifrelemeYontemleri(text)
    
    if (islem == "1"):
        print(dilkontrol.Cumlelere_ayir())
        
    elif (islem == "2"):
        print(dilkontrol.Kelimelere_Ayir())
        
    elif (islem == "3"):
        print(dilkontrol.Kac_adet_SesliHarf())
        
    elif (islem == "4"):
        print(dilkontrol.Buyuk_Unlu_Uyumu())
        
    elif (islem == "5"):
        print(dilkontrol.Buyukharf_Bul())
        
    elif (islem == "6"):
        print(sifreleme.MD5_Sifrele())
        
    elif (islem == "7"):
        print(sifreleme.SHA256_Sifrele())
        
    elif (islem == "8"):
        print(sifreleme.Blake2_sifrele())
    
    elif (islem == "9"):
        print(sifreleme.Whırl_Pool())

    elif (islem == "10"):
        print(sifreleme.RIPEMD160_Sifrele())
        
    elif (islem == "11"):
        print(sifreleme.SHA3_224_Sifrele())
        
    elif (islem == "12"):
        print(sifreleme.DES_Sifrele())
        
    elif (islem == "13"):
        print(sifreleme.AES_Sifreleme())
        
    else:
        print("Gecersiz Islem")
