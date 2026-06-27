list1 =[10,20,30,40,50]
list2 = [30,50,60,40,90]
common = []
for item in list1 :
    if item in list2:
        common.append(item)
print("common elements: ",common)        