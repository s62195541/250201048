import time 
def simple_timer(t):
  if t!=0:
   print('Remaining time:',t)
   time.sleep(1)
   return  simple_timer(t-1)
  else:
    print('Time is up!')
    return None

print(simple_timer(5))