unit=input("Enter the number of units consumed : ")
if unit<=150:
    bill=unit*2.40
elif unit>150 and unit<=300:
    bill=(150*2.40)+(unit-150)*3
else:
    bill=(150*2.40)+(150*3)+(unit)
    print bill