print("===== Welcome To Restaurant =====")

total_bill=0

while True:
    print("\nMENU")
    print("1. Pizza    - ₹200")
    print("2. Burger   - ₹100")
    print("3. Sandwich - ₹80")
    print("4. Sprite   - ₹20")
    
    choice=int(input("Enter Your chouce(1-4: "))
    quantity=int(input("Enter Qunatity: "))
    
    if choice==1:
        item="Pizza"
        price=200
    
    elif choice==2:
        item="Burger"
        price=100
    
    elif choice==3:
        item="Sandwich"
        price=80
        
    elif choice==4:
        item="Sprite"
        price=20
        
    else:
        print("Invalid choice!")
        continue
    
    cost=price*quantity
    total_bill=total_bill+cost
    
    print(f"{item} x {quantity} = ₹{cost}")
    print(f"current Total=₹{total_bill}")
    
    more=input("Do u want to order more? (y/n): ")
    
    if more.lower()!='y':
        break
    
    discount=0
    if total_bill>=1000:
        discount=total_bill*10/100
        
    bill_after_discount=total_bill-discount
    
    gst=bill_after_discount*18/100
    
    final_bill=bill_after_discount+gst
    
    print("\n===== FINAL BILL ======")
    print("Total bill       : ₹", total_bill)
    print("Discount         : ₹", discount)
    print("Bill After Disc  : ₹", bill_after_discount)
    print("GST (18%)        : ₹", gst)
    print("Final Amount     : ₹", final_bill)
    print("==============================")
    print("Thank You! Visit Again 😊")
    