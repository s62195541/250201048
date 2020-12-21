def harmonic(n):
  if n!=0:
    return 1/n + harmonic(n-1)
  else:
    return 0
harmonic(5)

print(harmonic(5))