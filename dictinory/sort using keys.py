mydict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
nd={}
result =sorted(mydict.keys())

for i in result:
    nd[i]=mydict[i]

print(nd)