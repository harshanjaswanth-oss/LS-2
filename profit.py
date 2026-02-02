costprice=int(input("costprice"))
sellingprice=int(input("sellingprice"))
if costprice>sellingprice:
   loss=costprice-sellingprice
   print ("Loss",loss)
else:
 profit=sellingprice-costprice
 print ("profit",profit)