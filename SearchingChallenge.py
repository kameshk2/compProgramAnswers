# keep this function call here 
def SearchingChallenge(strParam):

  # code goes here
  newDict={}
  count=0
  for x in strParam:
    if newDict.get(x) != None:
      count = newDict[x] + 1
      newDict[x]=count
    else:
      newDict[x]= 1
    
  print(newDict.items())

  chalToken="f18mag72r3c"
  for y in strParam:
    if newDict.get(y)==1:
      strParam = y + ":" + chalToken[::-1]
      break

  return strParam

print(SearchingChallenge('abcdef'))
