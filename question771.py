file = str(open('text1.txt','r').read())
arr = [ s.rstrip('\n').lower() for s in file.split('.')]
count = {}
for line in arr:
    tmp = {}
    line = line.replace(',',' ').replace('\n','').split()
    for word in line:
        if word not in tmp:
            tmp[word]=1 
    # print(tmp)
    for word in tmp:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    # print()
out = {}
for i in count:
    if count[i] > 10:
        out[i] = count[i]
print(out)