books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
di = {}
for book in books:
    book.replace(' ','')
    values=[]
    count=0
    for char in range(len(book)):
        count+=1
    values.append(count)
    uni=[]
    for unichar in book:
        if unichar not in uni:
            uni.append(unichar)
    values.append(len(uni))  
    tuple(values)
    
    di[book]=values

for up in di.values():
    list(up)
    avg=0
    for a in up:
        avg+=a
        avg = avg/len(up)
        int(avg)
        up.append(avg)
    
    for j in di.keys():
        di[j]=up
    
print(di)