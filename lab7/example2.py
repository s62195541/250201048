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

print(di)
    