

from datetime import datetime
name = input("Enter your Name: ")

lists = """
      Rice Rs 20/kg
     Sugar Rs 30/kg
      Salt Rs 20/kg
       Oil Rs 80/kg
    Paneer Rs 110/kg
     Maggi Rs 50/kg
     Boost Rs 90/each
   colgate Rs 85/each
  """

price = 0
pricelist = ()
totalprice = 0
Finalprice = 0
Itemlist = []
Quantitylist = []
plist = []

items ={
       "Rice": 20,
      "Sugar": 30,
       "Salt": 20,
        "Oil": 80,
     "Paneer": 110,
      "Maggi": 50,
      "Boost": 90,
    "Colgate": 85
}

option = int(input("For list of items press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1= int(input("If you want to buy press 1 or 2 for exist:"))
    if inp1 == 2:
        break
    elif inp1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter Quantity: "))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append(item,quantity,price)
            totalprice += price
            Itemlist.append(item)
            Quantitylist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5)/100
            Finalprice = gst + totalprice
        else:
            print(" Sorry,You entered item is not available ")
    else:
        print("you entered wrong number")

inp = input("can I bill the items yes or no:")
if inp.lower() == "yes":
    if Finalprice !=0:
        print(25*"=","ADDANKI SUPERMARKET",25*"=")
        print(28*" ", "ADDANKI")
        print("NAME: ",name,28*" ","DATE: ", datetime.now())
        print(70*"-")
        print("S.No",10*" ","ITEM",10*" ","QUANTITY",4*" ","PRICE")
        for i in range(len(pricelist)):
            print(i+1,15*" ",Itemlist[i],15*" ",Quantitylist[i],4*" ",plist[i])
        print(70 * "-")
        print(50*" ","TOTAL AMOUNT: Rs", totalprice)
        print("GST AMOUNT",45*" ","Rs",gst)
        print(70 * "-")
        print( 30 *" ","THANKS FOR VISITING")
        print(70 * "=")
    else:
        print("Please buy items to generate the bill")


