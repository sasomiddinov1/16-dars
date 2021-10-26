# -*- 16-dars NasTing -*-
"""
Created on Tue Oct 26 16:20:36 2021

@author: SAYFIDDIN
"""

# #Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# #ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
# #va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

temur = {
    'ism': 'Amir Temur ibn Amir Taragʻay',
    'tyil': 1336,
    'vyil': 1405,
    'tjoy': ' Shahrisabz'
    
    
    }

a_navoi = {
    'ism': 'Alisher Navoiy',
    'tyil': 1441,
    'vyil': 1501,
    'tjoy': 'Shahrisabz'
    
    
    }

hamid_olimjon = {
    'ism': 'Hamid Olimjon',
    'tyil': 1909,
    'vyil': 1944,
    'tjoy': 'Jizzax'
    
    }

steven = {
    'ism': 'Steven Paul',
    'tyil': 1955,
    'vyil': 2011,
    'tjoy': 'AQSh'
    
    }



shaxslar = [temur, a_navoi, hamid_olimjon, steven]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    tjoy = shaxs['tjoy']
    
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
          f"{vyil-tyil} yil umr ko'rgan.")


# #Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
 ## For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.


temur = {
    'ism': 'Amir Temur ibn Amir Taragʻay',
    'tyil': 1336,
    'vyil': 1405,
    'tjoy': ' Shahrisabz',
    'haqida': ['Sarkarda, markazlashgan davlat asoschisi, ilm-fan va madaniyat homiysi']
    
    }

a_navoi = {
    'ism': 'Alisher Navoiy',
    'tyil': 1441,
    'vyil': 1501,
    'tjoy': 'Shahrisabz',
    'haqida': ['«Nizomiddin Mir Alisher»', '«Qush mantigʻi»', ' «Mantiq ut–tayr»']
    
    
    }

hamid_olimjon = {
    'ism': 'Hamid Olimjon',
    'tyil': 1909,
    'vyil': 1944,
    'tjoy': 'Jizzax',
    'haqida': ["shoir, publitsist, adabiyotshun"]
    
    }

steven = {
    'ism': 'Steven Paul',
    'tyil': 1955,
    'vyil': 2011,
    'tjoy': 'AQSh',
    'haqida': ['Apple Inc. asoschisi']
    
    }



shaxslar = [temur, a_navoi, hamid_olimjon, steven]

for shaxs in shaxslar:
    ism = shaxs['ism']
    haqida = shaxs['haqida']
    print(f"\n{ism} haqida malumot: ")

    for asar in haqida:
        print(asar)

# #Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
 ## Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga
# # saqlang.  Natijani konsolga chiqaring.

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }


for ism, kinolar  in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:") 
    for kino in kinolar:
        print(kino)

# #Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida
 ## ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni
# # konsolga chiqaring.



davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    } 



for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")



# #Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
# #foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning
 ## lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan
# # xabarni chiqaring.

davlat = input('Davlat nomini kiriting: ').lower()


if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")














