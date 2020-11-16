password = 'abc123'

guess = input('Enter a password!')

if guess=='help':
  print(password[0])
elif guess==password:
  print('Welcome')
else:
  print('Wrong')