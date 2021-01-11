class Employee:
  def __init__(self,name,salary):
    self.set_name(name)
    self.set_salary(salary)
  def get_name(self):
    return self.name
  def set_name(self):
    if len(name)!=0:
      self.name=name
  def get_salary(self):
    return self.salary
  def set_salary(self):
    if salary>0:
      self.salary=salary
  def info(self):
    print(f'{name}:{salary}')
Employee('ibo',1231)