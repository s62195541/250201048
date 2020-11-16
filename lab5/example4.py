password = 'abc123'



while True:
  guess = input('Enter a password!')
  if guess=='help':
    print(password[0])
  elif guess==password:
    print('Welcome')
  else:
    print('Wrong')