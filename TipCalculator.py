print("Tip Calculator")

bill_amount = int(input("what is your total bill amount? : $"))
tip_amount = int(input("what is amount of tip you want to add? : $"))
num_of_people = int(input("How many people to split the bill? :"))
total_tip = bill_amount*tip_amount/100
final_amount = (bill_amount + total_tip)/num_of_people
print("Each person needs to pay : $",round(final_amount,2))