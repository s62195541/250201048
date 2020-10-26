number1 = float(input('Enter a number::'))
number2 = float(input('Enter a number::'))
number3 = float(input('Enter a number::'))

if number1<number2:
  if number1<number3:
    print(number1)
  else:
    print(number2)
else:
  if number2<number3:
    print(number2)
  else:
    print(number3)