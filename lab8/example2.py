def is_prime(n):
  if n>1:
    for i in range(2,n+1):
      if n%i!=0:
        return True
      else:
        return False
  else:
    return False

def print_primes_between(n1,n2):
  for i in range(n1,n2):
   if is_prime(i):
    print(i)

def main():
  n1=int(input('Enter a number'))
  is_prime(n1)
  
  n2=int(input('Enter a number'))
  is_prime(n2)

  print_primes_between(n1,n2)
main()