#forming a sample MAC address from the API frames received from XBee module
a=['0x13','0xa2','0x0','0x40','0xbc','0xdb','0x9a']#sample frames to be contained in received data
add=[]
address= ( int(0x13a20040bcdb9a))
address=("%x" % address) #remove '0x' from beginning and L at end
print address
a=[int(x,16) for x in a] #convert the sample frame data to integer
add.append((a[5]<<8)|a[6])#combine '0xdb' and '0x9a' to form 'oxdb9a'
p=4
q=16
r=0
for i in range(0,5):      #perform appending using loop
    add.append((a[p]<<q)|add[r])
    p=p-1
    q=q+8
    r=r+1
a=str("%x" % add[-1])
print a
if address==a:
    print 'correct address'
else:
    print 'different address'
    
