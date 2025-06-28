#hobi = "berenang, gitar, ngoding, membaca alquran"
#print(hobi)

hobbies = ["berenang", "gitar", "ngoding", "membaca alquran"]
#startFrom = 1
#print(hobbies[3 - startFrom])

tmp_hobbies = hobbies

# print(f"hobbies -> {hobbies}")
# print(f"tmp_hobbies -> {tmp_hobbies}")
print("hobbies", "->", hobbies)

print(type(hobbies))

# *
# **
# ***
# ****    
# for i in range(5)
#     print(i+1)

# List of different data types
#data = [, "Hello", 3.14, True, [1, 2, 3], {"key": "value"}]

# Iterate through the list and check the type of each element
for item in data:
    print(f"The type of {item} is {type(item)}")

for x in y :
    # syarat 1
    print() # kalau berhasil ulang, kalau gagal lanjut
    for y in z :
        # syarat 2
        print() # kalau berhasil balik ke atas, kalau gagal stop
        
 for i in range(1, height + 1):
        # Print leading spaces
        spaces = ' ' * (height - i)
        # Print True values
        for j in range(2 * i - 1):
            print("True", end="")  # Print 'True' without new line
        print()  # Move to the next line after each row