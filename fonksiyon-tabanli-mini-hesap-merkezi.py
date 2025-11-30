#toplama fonksiyonu
def sum_numbers( num1, num2):
    return num1+num2

#çıkarma fonksiyonu
def subtraction( num1, num2):
    return num1-num2

#çarpma fonksiyonu
def multiply( num1, num2):
    return num1*num2

#bölme fonksiyonu
def divide( num1, num2):
    if num2!=0:
        return num1/num2
    else:
        print("Payda sifir iken bölme işlemi tanimsizdir.")

#faktöriyel fonksiyonu
def factorial (num1):
    if num1<0:
        print("Negatif sayilarin faktöriyeli tanimsizdir.")
    elif num1 == 0 or num1 == 1:
        return 1
    else:
        return num1*factorial(num1-1)

#asal sayi kontrol fonksiyonu
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):  # 2'den başlayıp num-1'e kadar kontrol ediyoruz
        if num % i == 0:
            return False
    else:
        return True
    
#ortalama fonksiyonu
def average(mylist):
    toplam = 0
    adet = 0
    for n in mylist:
        toplam += n
        adet += 1
    if adet == 0:
        return 0  # boş listeyi önlemek için
    return toplam / adet


while True:
    print("------------------HESAP MERKEZİ-----------------------")
    print("1-Toplama hesabi için seçiniz.")
    print("2-Çikarma hesabi için seçiniz.")
    print("3-Çarpma hesabi için seçiniz.")
    print("4-Bölme hesabi için seçiniz.")
    print("5-Faktöriyel hesabi için seçiniz.")
    print("6-Asal sayi kontrolü için seçiniz.")
    print("7-Ortalama hesabi için seçiniz.")
    print("8-Çikiş yapmak için seçiniz.")
    print("------------------------------------------------------")

    secim=input("Seçiminizi giriniz:")



    if secim == "1":
        print("Toplanmasi istenilen sayilari giriniz")
        num1=float(input("Birinci sayiyi giriniz:"))
        num2=float(input("İkinci sayiyi giriniz:"))
        print(sum_numbers(num1,num2))

    elif secim == "2":
        print("Çikarilmasi istenilen sayilari giriniz")
        num1=float(input("Birinci sayiyi giriniz:"))
        num2=float(input("İkinci sayiyi giriniz:"))
        print(subtraction(num1,num2))

    
    elif secim == "3":
        print("Çarpilmasi istenilen sayilari giriniz")
        num1=float(input("Birinci sayiyi giriniz:"))
        num2=float(input("İkinci sayiyi giriniz:"))
        print(multiply(num1,num2))

    
    elif secim == "4":
        print("Bölünmesi istenilen sayilari giriniz")
        num1=float(input("Birinci sayiyi giriniz:"))
        num2=float(input("İkinci sayiyi giriniz:"))
        print(divide(num1,num2))


    elif secim == "5":
        num1=int(input("Faktöriyeli hesaplanacak sayiyi giriniz:"))
        print(factorial(num1))

    
    elif secim == "6":
        num1=int(input("Asalliği kontrol edilecek sayiyi giriniz:"))
        print(is_prime(num1))

        

    elif secim == "7":
        liste = input("Sayilari boşluk birakarak giriniz:").split()
        liste = [float(x) for x in liste]
        print(average(liste))
    
    elif secim =="8":
        print("Çikiş yapiliyor...")
        break
    
    else:
        print("Geçersiz seçim.")






