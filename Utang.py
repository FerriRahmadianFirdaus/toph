#def
 
# limit = 200000

# def money() :
#     try :
#         cash = int(input("masukkan uang Anda: "))
#     except ValueError :
#         print("Masukkan angka yang valid!")
#         return money()
    
    
#     if cash == limit :
#         print("Uang pas")
#     elif cash > limit :
#         print("Uang Anda lebih, ini kembaliannya ", cash - limit)
#     else :
#         print("Uang kurang ", limit - cash)

# money()

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
# greet("Bob")
# greet("Charlie")

import random

welcome_message = "WELCOME TO REVOLUTION!"
revolutionPosition = random.randint(1, 5)

print('''
********************************''')
print("****",welcome_message,"****")
print('''********************************      
''')

namaUser = input("Masukan nama anda: ")

print(f'''
Hallo {namaUser} Perhatikan gambar dibawah ini !
^_^  >_<  :)  :>  :]''')

def ho() :
    while True :
        PilihanAbah = input('''
Menurut anda senyum siapa yang paling indah? [1 / 2 / 3 / 4 / 5]: ''')      
        try:
            PilihanUser = int(PilihanAbah) 
            if PilihanUser in [1, 2, 3, 4, 5] :
                print(f'''
Pilihan anda adalah: {PilihanUser}''')
                return
            else :
                print("jawaban invalid")
        except ValueError :
            print("jawaban invalid")
ho()

if PilihanUser == revolutionPosition:
    print(f'''
Congratulations {namaUser} ! ! !
Senyum terindah berada di nomor {revolutionPosition}
''')
else :
    print(f'''
Nice Try {namaUser} 
Sayangnya senyum terindah berada di nomor {revolutionPosition} dan pilihanmu {PilihanUser}

Jangan berhenti mencoba ! ! !
''')