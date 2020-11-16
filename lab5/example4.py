password = 'abc123'

guess = input('Enter a password!')

while True:
  if guess=='help':
    print(password[0])
  elif guess==password:
    print('Welcome')
  else:
    print('Wrong')