#Imports
from datetime import datetime

days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
disc = False
diff = False
total = False

def tax(amount):
    return (amount/100)*106

def disc_day(daynum):
    return days[daynum] == "tue" or days[daynum] == "wed"
#Stretch 2
q = input("Enter number of items:")
data = input("Enter price of item:")
while int(data) != 0:
    total += int(data)*int(q)
    q = input("Enter number of items:")
    data = input("Enter price of item:")

#Core 1
#total = int(input("Enter Subtotal:"))
day = datetime.now().weekday()

#Core 2
if total >= 50 and disc_day(day):
    disc = (total/10)*9

#Core 3
if disc == False:
    end = tax(total)
elif disc:
    end = tax(disc)

#Stretch 1
if disc_day(day) and total < 50:
    diff = 50 - total

#Output
print(f"Total: {total}")
if disc:
    print(f"Discounted: {disc}")
if diff:
    print(f"Under discount by: {diff}")
print(f"End Total: {end}")
