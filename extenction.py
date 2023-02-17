import sys
newList = ['n', 0, 8]
for data in newList:
    try:
        print("Hasilnya :", data)
        x = 1/int(data)
        break
    except Exception as e:
        print("Maaf!", e.__class__)
        print("Data selanjutnya.")
        print()
print("Inversenya", data, "adalah", x)