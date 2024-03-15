class Python_Switch:
   def day(self,month):
    default = "Incorrect day"
    return getattr(self,'case_'+ str(month),lambda:default)()
  
   def case_1(self):
    return "jan"
  
   def case_2(self):
    return "feb"
  
   def case_3(self):
    return "mar"
  
switch_instance = Python_Switch()

print(switch_instance.day(3))