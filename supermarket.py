from datetime import datetime
name=input("Enter your name:")
#LIST of items
lists='''
Rice      Rs 20/kg
Sugar     Rs 30/kg
Salt      Rs  20/kg
oil       Rs  120/liter
paneer    Rs 110/kg
Gulab jam Rs 120/kg
Maggi     Rs 50/kg
Boost     Rs 90/each
Colgate   Rs 55/each
'''
#Declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
list=[]
qlist=[]
#rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':120,'paneer':110,'gulab jam':120,'maggi':50,'boost':90,'colgate':55}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            qlist.append(quantity)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enterd item is not available")
    else:
        print("you enterd wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","kumar supermarket",25*"=")
            print(28*" ","kakinada")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,3*' ',qlist[i])
            print(75*"-")
            print(50*" ",'Totalamount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")