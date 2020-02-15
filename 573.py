file = str(open('text2.txt','r').read())
arr = [ s.rstrip('\n').lower() for s in file.split(' ')]
mid = len(arr)//2
left = arr[0:mid]
rigth = arr[mid:len(arr)+1]

first = ""
second = ""
for word in left:
    first+=word+" "
for word in rigth:
    second+=word+" "

# # ต้นไฟล์2
print("ต้นไฟล์")
print(first)

# # ท้ายไฟล์2
print("ท้ายไฟล์")
print(second)





