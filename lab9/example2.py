def get_reversed(alist):
  if len(alist)==1:
    return alist
  return alist[-1:] + get_reversed(alist[0:-1:1])  
print(get_reversed([1,2,3,4,5]))