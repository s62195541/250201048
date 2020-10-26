age = int(input('How old are you ?'))
price = 3 

if age<6 or age>60:
  print('Free')
elif 6<=age<18:
  print('%50 discount 1.5 TL')
else: 
  print('Regular charge 3 TL')