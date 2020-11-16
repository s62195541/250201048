N = int(input('How many numbers do yo want?'))
count = 0
for i in range(N):
  number = int(input('Enter a number!'))
  if number%2==0:
    count = count + 1
print((count/N)*100,'%' )