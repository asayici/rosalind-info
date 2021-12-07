#INI3
def sliceStr(strX, a,b,c,d):
  return strX[a:b+1]+" "+strX[c:d+1]

strX = "Write the desired string here"
a = 29 
b = 35 
c = 77 
d = 81 
print(sliceStr(strX, a,b,c,d))