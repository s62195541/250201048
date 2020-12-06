em_di={}

for i in range(5):
    name= input('enter a employee name:')
    salary=int(input('enter a salary of empoyee:'))
    em_di[name]=salary
    
best_three=sorted(em_di.values())[-3:]
for name in em_di:
   salary = em_di[name]
   if salary in best_three:
       print(name)