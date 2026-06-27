word = input("Enter word: ")
file = open("sample.txt", "r")
data = file.read()
if word in data:
    print("Found")
else:
    print("Not Found")
file.close()