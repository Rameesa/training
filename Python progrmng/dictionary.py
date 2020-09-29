mydict = {'id':12, 'name':'rami','age':22, 'place':'clt'}
print(mydict['id'])
mydict['age']=25
mydict['lastname'] = 'savad'

print(mydict)
for data in mydict:
    print (mydict[data]) #returns value
for data in mydict:
    print(data) #returns key
for data in mydict.values():
    print(data)         #returns values in mydict
for data in mydict.items():
    print(data)         #rerurns each keyvalue pair
for k,v in mydict.items():
    print(k, ':',v)   #returns keyvalue in given format ie, k:v