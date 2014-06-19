"""#forming a sample MAC address from the API frames received from XBee module"""

a=['0x13','0xa2','0x0','0x40','0xbc','0xdb','0x9a']
add=[]
address= ( int(0x13a20040bcdb9a))
address=("%x" % address)
print address
a=[int(x,16) for x in a]
add.append((a[5]<<8)|a[6])
p=4
q=16
r=0
for i in range(0,5):
    print i
    print q
    add.append((a[p]<<q)|add[r])
    p=p-1
    print p
    q=q+8
    print q
    r=r+1
    print r
a=str("%x" % add[-1])
print a
if address==a:
    print 'correct address'
else:
    print 'different address'
    
