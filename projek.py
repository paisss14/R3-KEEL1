# Ngetes aja ini bang ntar dihapus aja wkwkw
n = int(input())

for i in range(1,n + 1):
    if i == n:
        print("Kapal Karam")
    elif i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 11 == 0:
        print("DPA Asiq")
    else:
        print(i)