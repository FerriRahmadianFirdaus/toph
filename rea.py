#1

# hobi = "membaca alquran, berenang, ngoding"
#print(hobi)

hobbies = ["membaca alquran", "berenang", "ngoding", "main gitar", "x", "y"]
#index = 1
#print(hobbies[2 - index])

#2
tmp_hobbies = hobbies

print(f"hobbies -> {hobbies}")

#3 Memanipulasi Array
tmp_hobbies[1 + 2] = "billiar"

print(f"tmp_hobbies -> {tmp_hobbies}")

#4 Data jutaan ->len(menghitung data)
print(len(hobbies))

l_data = len(hobbies) - 1
print(hobbies[l_data])

print(hobbies[len(hobbies) - 1])

#hobbies = blablabla
bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 3 #ini tetep harus kosong
goa = goa_kosong.copy() #ini adalah tempat baru untuk cuypay

goa[3] = "|0_0|"

print(goa)
#print(f"")

#pr cuypay muncul di setelah
#shallow copy akan selalu terpakai
 
#pr join_array

