a = {'jan doe' : '+27 555 5367', 'jhon smith' : '+27 555 6254', 'bob stone' : '+27 555 5689'}

a['jane doe']='+27 555 1024'

a.keys()
a.values()
a.items()

a['anna cooper']='+27 555 3237'

print ('bob stone', a['bob stone'])

for k in a.keys():
    print (k)
    
for v in a.values():
    print (v)

for k.v in a.items():
    print (k,v)
    
