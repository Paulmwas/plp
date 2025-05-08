# discount(price, discpercentage)
# if disc > 20 --->apply it --> if nnot dont apply
# Prompt the user to key in the price and disc percent then perrform the above
price = int(input("Please enter the price of the product:\n"))
discount_percentage = int(input("Please provide the discount: \n"))
def calculate_discount(price, discount_percentage):
    if discount_percentage<20:
        print(price)
    else:
        payment_price =(((100 - discount_percentage)/100)*price)
        print(f"Hey Wonderful Customer You will pay Ksh:{payment_price}")


calculate_discount(price,discount_percentage)