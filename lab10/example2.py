def hailstone(n):
  s =  str(n)
  if n==1:
    return s
  else:
    if n%2==0:
      return s+','+ hailstone(n//2)
    else:   
      return s+',' + hailstone((3*n)+1) 
print(hailstone(5))