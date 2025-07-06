#FIRST PYTHON

import random

welcome_message = "WELCOME TO REVOLUTION!"
revolutionPosition = random.randint(1, 5)

print('''
         ******''')
print("        ************")
print("     ******************")
print("  ************************")
print("**",welcome_message,"**")
print("  ************************")
print("     ******************")
print("        ************")
print('''           ******
                    ''')

namaUser = input("Masukan nama anda : ")

print(f'''
Hallo ... {namaUser} 
Perhatikan gambar dibawah ini !
 >_<   :)   :>   :]  ^_^''')

while True :
    PilihanAbah = input('''
Menurut anda senyum terindah berada di nomor berapa? 1 / 2 / 3 / 4 / 5 : ''')      
    try:
        PilihanUser = int(PilihanAbah) 
        if PilihanUser in [1, 2, 3, 4, 5] :
            print(f'''
Pilihan anda adalah : {PilihanUser}''')
            break
        else :
            print("jawaban invalid")
    except ValueError :
        print("jawaban invalid")
   
#Yes or No
while True:
    Detition = input('''
Apakah anda yakin ? Yes/No : ''')
    if Detition in ["yes", "ya", "y", "yap", "yo", "yut", "Yes", "Ya", "Y", "Yo"]:
        break
    elif Detition in ["no", "tidak", "n", "tak", "No", "N", "Tidak" ]:
        while True :
            PilihanAbah = input('''
Menurut anda senyum terindah berada di nomor berapa? 1 / 2 / 3 / 4 / 5 : ''')
            try:
                PilihanUser = int(PilihanAbah) 
                if PilihanUser in [1, 2, 3, 4, 5] :
                    print(f'''
Pilihan anda adalah : {PilihanUser}''')
                    break
                else :
                    print("jawaban invalid")
            except ValueError :
                print("jawaban invalid")
    else :
        print("jawaban invalid")

if PilihanUser == revolutionPosition:
    print(f'''
Congratulations {namaUser} ! ! !
Senyum terindah berada di nomor {revolutionPosition}
''')
else :
    print(f'''
Nice Try {namaUser} 
Sayang sekali senyum terindah berada di nomor {revolutionPosition} dan pilihanmu adalah {PilihanUser}

Jangan berhenti mencoba ! ! !
''')

#Soal 1    
import sys

while True :
    PilihanSetuju = input('''Apakah anda ingin lanjut ? : ''')
    if PilihanSetuju in ["yes", "ya", "y", "yap", "yo", "yut", "Yes", "Ya", "Y", "Yo"]:
        break
    elif PilihanSetuju in ["no", "tidak", "n", "tak", "No", "N", "Tidak" ] :
        print (f'''
Terima Kasih {namaUser} sudah bermain ...
                    ''')
        sys.exit()
    else :
        print('''Jawaban Invalid
              ''')
#else akan selalu looping sampai if & else terpenuhi
#Soal 1
while True :
    PilihanMu = input('''
Pertanyaan Pertama...

  a. Boniex Nurwega
  b. Ferry Irwandi
  c. Ari Lesmana
  d. Rio Clappy

Dari 4 nama diatas siapakah pelantun lagu Bunga Abadi ? : ''')
    if PilihanMu in ["Rio Clappy", "d", "D", "rio clappy", "Rio", "rio"] :
        print ('''
Selamat jawaban anda benar
                ''')
        break
    elif PilihanMu in ["A", "a", "B", "b", "C", "c", "D", "d", "Boniex Nurwega", "boniex nurwega", "Ferry Irwandi", "ferry irwandi", "Ari Lesmana", "ari lesmana", "boniex", "Ari", "ari", "Boniex", "ferry", "Ferry"] :
        print ('''
Maaf... jawaban yang benar adalah d. Rio Clappy
                ''')
        break
    else :
        print('''jawaban invalid
                ''')
while True :
    PilihanSetujuDua = input('''Apakah anda ingin lanjut ? : ''')
    if PilihanSetujuDua in ["yes", "ya", "y", "yap", "yo", "yut", "Yes", "Ya", "Y", "Yo"]:
        break
    elif PilihanSetujuDua in ["no", "tidak", "n", "tak", "No", "N", "Tidak" ] :
        print (f'''
Terima Kasih {namaUser} sudah bermain ...
                ''')
        sys.exit()
    else :
        print('''Jawaban Invalid
              ''')
        
while True :
    PilihanKedua = input ('''
Pertannyaan Kedua...

a. Dota 2
b. Mobile Legend
c. Arena of Valor
d. Free Fire

Dari pilihan diatas manakah yang bukan termasuk game MOBA ? : ''')
    if PilihanKedua in ["Free Fire", "free fire", "FF", "ff", "d", "D", "FREE FIRE"] :
        print ('''
Selamat Jawaban Anda benar...
                ''')
        break
    elif PilihanKedua in ["a", "A", "b", "B", "c", "C", "Dota 2", "dota 2", "dota", "Dota","DOTA", "DOTA 2" "ML", "ml", "Ml" "Mobile Legend", "mobile legend", "MOBILE LEGEND", "AOV", "aov", "Arena of Valor", "arena of valor", "Arena Of Valor"] :
        print ('''Jawaban Anda salah... Free Fire bukan termasuk game MOBA''')
        break   
    else :
        print ('''Jawaban Invalid
                ''')
print ('''Terima Kasih telah bermain
       ''')
