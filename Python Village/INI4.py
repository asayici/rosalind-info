#INI4
def sumOdds(a, b):
  res = 0
  for i in range(a,b+1):
    if i%2 != 0:
      res = res + i 
  return res 

#Set values to variables a and b
a=4675 
b=8929
print(sumOdds(a,b))