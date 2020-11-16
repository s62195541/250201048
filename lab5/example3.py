number1 = input('Enter a number!')
number2 = input('Enter a number!')
count = 0
for i in range(len(number1)):
  for j in range(len(number2)):
    if number1[-i]==number2[-j]:
      count = count + 1

print(count)
