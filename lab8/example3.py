import random
def get_rand_list(b,e,N):
  rand_list=random.sample(range(b, e), N)
  return rand_list

def get_overlap(rand_list1,rand_list2):
  overlap=[]
  for i in rand_list1:
    if i in rand_list2:
      overlap.append(i)
  return overlap
     
def main():
  rand_list1=get_rand_list(0,10,5)
  rand_list2=get_rand_list(0,10,5)
  print(rand_list1)
  print(rand_list2)
  print(get_overlap(rand_list1,rand_list2))
main()