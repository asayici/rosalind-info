#INI6
strX = "When I find myself in times of trouble Mother Mary be Let it be let it be let it be let it be There will be an answer let "
strXwords = strX.split()
strXfreq = {}
for w in strXwords:
  if w not in strXfreq:
    strXfreq[w] = 1
  else:
    strXfreq[w] = strXfreq[w] + 1

for key in strXfreq:
  print(key, strXfreq[key])