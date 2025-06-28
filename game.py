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
#test username
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