ref_email = ceng113@iyte.edu.tr

email = input('Enter your email adress.:')
email = email.upper()
part1 = email.split('@')[0]
part1 = part1.replace('.','')
part2 = part1 + '@' + part2

print(email)    
    
    if ref_email==email:

      print(True)
    else:
      print(wrong)