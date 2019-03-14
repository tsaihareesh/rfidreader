import sys

productInfo = {"S8": "S8,samsung,10,500", "S9": "S9,samsui,10,600","Iphone6s": "Iphone6s,apple,10,600"}
uuidProductMapping = {"89:230:191:90":"S8","249:241:231:94":"S9","217:131:52:90":"S9","185:77:56:90":"Iphone6s","217:45:180:176":"S9"}

def input():
    uidSet = set()
    uidSet.add(str(1) + ":" + str(2) + ":" + str(3) + ":" + str(4))
    uidSet.add(str(11) + ":" + str(22) + ":" + str(33) + ":" + str(44))
    uidSet.add(str(111) + ":" + str(222) + ":" + str(333) + ":" + str(444))
    (bill,totalAmount) = generateBill(uidSet)

    print bill
    print totalAmount


def generateBill(uidSet):
    # item-id,description,price,qty,sku
    bill = {}
    for value in uidSet:
        itemId = uuidProductMapping.get(value)
        if itemId in bill:
            itemDetails = productInfo.get(itemId)
            billValue = bill.get(itemId)
            qty = int(getQuantity(billValue)) + 1
            price = int(getPrice(billValue)) * qty
            itemDetails =  getBillTag(itemDetails) +","+ str(price)+","+ str(qty)
            bill[itemId] = itemDetails
        else:
            itemDetails = productInfo.get(itemId)
            price = getPrice(itemDetails)
            qty = 1
            itemDetails = getBillTag(itemDetails) +"  \n \t Qty :"+ str(qty) + " \n \t Price :"+  str(price)
            bill[itemId] = itemDetails
    return bill


def getPrice(itemDetail):
  return itemDetail.split("Price :")[1]

def getEffectivePrice(itemDetail):
  return itemDetail.split("Price :")[1]

def getQuantity(bill):
  return (bill.split("Qty :")[1]).split(" ")[0]

def getBillTag(itemDetail):
    return " \t "+itemDetail.split(",")[0] + " \n \t make : "+itemDetail.split(",")[1] + " \n \t unit price : "+itemDetail.split(",")[3]

if __name__ == '__main__':
    globals()[sys.argv[1]]()