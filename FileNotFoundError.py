try:
    file = open("abc.txt","r")
except FileNotFoundError:
    print("File Not Found")