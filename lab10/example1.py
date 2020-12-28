def rec_multiplication(n):
  if n==0:
    return 0
  else:
    return 3 + rec_multiplication(n-1)

print(rec_multiplication(9))