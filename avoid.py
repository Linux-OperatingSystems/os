data={'p0':[10,743],'p1':[200,122],'p2':[302,600],'p3':[211,11],'p4':[2,433]}
req=332
proc=[]
i=len(data)
while (len(proc)<i):
    for pro,bts in data.items():
        if(bts[1]<=req):
            req=req+bts[0]
            proc.append(pro)if pro not in proc else proc
        else:
            i=len(data)
print(proc)


