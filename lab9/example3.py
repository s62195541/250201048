def get_evens(alist):
  if len(alist)!=0:
    if alist[0]%2==0:
      return 1 + get_evens(alist[1::])
    else:
       return 0 + get_evens(alist[1::])
  else:
    return 0
print(get_evens([0,1,2,3,4,5]))