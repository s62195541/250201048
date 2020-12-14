def binary_to_dec(n):
  n=str(n)[::-1]
  dec=0
  for i in range(len(n)):
    dec+=int(n[i])*(2**i)
  return dec

def dec_to_binary(n):
  binary=''
  while n>0:
    binary+=str(n%2)
    n//=2
  return binary[::-1]

def main():
  print(binary_to_dec('10010'))
  print(dec_to_binary(18))
main()


