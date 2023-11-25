gs =[]
tot = 0
for i in range(0,4):
    pname = input("Enter product name:")
    unit = int(input("Enter unit price:"))
    gst = int(input("Enter gst "))
    qty = int(input("Enter quantity:"))
    gstprice = (gst/100)*unit
    if unit>500:
        r = (unit*0.05)
        unit = unit - r
    
    tot+= (unit*qty)+gstprice
    gs.append(gstprice)
print("Total amount :",tot)
print(sorted(gs))


