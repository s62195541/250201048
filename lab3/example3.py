gpa = int(input('Enter your GPA::'))
nol = int(input('Enter numbur of your lecture::'))

if gpa<2:
  if nol<47:
    print('Not enough number of lectures and GPA')
  else:
    print('Not enough GPA')

else:
  if nol<47:
    print('Not enough number of lectures')
  else:
    print('Graduated')
