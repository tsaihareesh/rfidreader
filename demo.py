import sys

productInfo = {"S8": "S8,samsung,10,500", "S9": "S9,samsui,10,600"}
uuidProductMapping = {"89:230:191:90":"S8","249:241:231:94":"S9","217:131:52:90":"S9"}

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
            itemDetails = itemDetails +","+ str(price)+","+ str(qty)
            bill[itemId] = itemDetails
        else:
            itemDetails = productInfo.get(itemId)
            price = getPrice(itemDetails)
            qty = 1
            itemDetails = itemDetails +","+ str(price)+","+str(qty)
            bill[itemId] = itemDetails
    return bill


def getPrice(itemDetail):
  return itemDetail.split(",")[3]

def getEffectivePrice(itemDetail):
  return itemDetail.split(",")[4]

def getQuantity(bill):
  return bill.split(",")[5]




if __name__ == '__main__':
    globals()[sys.argv[1]]()