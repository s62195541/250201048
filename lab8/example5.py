def password_checker(password):
  level=0
  letters=0
  numbers=0
  specials=0
  if len(password)<8:
    level=0
  else:
    for i in password:
      if i.isalpha()==True:
        letters+=1
      elif i.isnumeric()==True:
        numbers+=1
      else:
        special+=1
  if letters>0:
    level+=1
  if numbers>0:
    level+=1
  if special>0
    level+=1
  return level

def main():
  password=input('Enter your password:')
  print(password_checker(password))
main()
