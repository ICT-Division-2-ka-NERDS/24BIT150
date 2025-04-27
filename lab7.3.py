data=[{"d":1,"e":1,"s":200,},
      {"d":1,"e":2,"s":2005},#d=department number,e=employee number,s=salary
      {"d":2,"e":2,"s":2000},
      {"d":3,"e":3,"s":20000},
      {"d":4,"e":4,"s":200000},]
ds={}#department salary
for i in data:
    d=i['d']
    s=i['s']

    if d not in ds:
        ds[d]=[s,s]#[min,max]

    else:
        ds[d][0]=min(ds[d][0],s)
        ds[d][1]=max(ds[d][1],s)

for d,s in ds.items():
    print(f"d {d} -> Min: {min(s)}, Max: {max(s)}")
