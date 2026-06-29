price=int(input("enter price."))
discount=int(input("enter discount (%)."))
discount_amount=(price*discount)/100
final_price=price-discount_amount
print("discount=",discount_amount)
print("final=",final_price)
