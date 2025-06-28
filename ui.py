# welcome_message = "welcome to revolution!"

# print("****************************")
# print(f"** {welcome_message} **")
# print("****************************")

# nomorSaya = 17

# if nomorSaya == 4:
#     print("yes you are the reason 4me")
# else: 
#     print("hiks you are not 4me")

# usia1 = 17
# usia2 = "17"
# usia3 = 81

# print(type(usia1))
# print(type(usia2))
# print(type(usia3))

# namaUser = input("masukan nama anda: ")

# print(f'''
# Hallo {namaUser}! jangan perhatikan gambar dibawah ini
# :) :) :) :)
# ''')

# PilihanUser = input("menurut anda senyum siapa yang lebih indah? [1 / 2 / 3 / 4]")

# print(f"pilihan anda adalah {PilihanUser}")
while True :
    PilihanAbah = input("menurut anda senyum siapa yang lebih indah? [1 / 2 / 3 / 4 / 5]: ")
    try:
        PilihanUser = int(PilihanAbah) 
        if PilihanUser in [1, 2, 3, 4, 5] :
            print("pilihan anda adalah:", PilihanUser)
            break
        else :
            print('''jawaban invalid
                ''')
    except ValueError :
        print('''jawaban invalid
                ''')