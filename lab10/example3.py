def sum_of_list(alist):
  if len(alist)==0:
    return 0 

  else:
    if isinstance(alist,list)==False:
      return alist[0] + sum_of_list(alist[1:])
    else:
      if len(str(alist[0]))==1:
        return alist[0]+ sum_of_list(alist[1:])
      else:
        return alist[0][0]+ sum_of_list(alist)

print(sum_of_list([3,12,76,[4,56,43],[2,8],81,75]))