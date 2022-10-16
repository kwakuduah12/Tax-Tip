# A simple interactive program that alerts consumers of their tax and the minimum tip they can give
cost = int(input('meal cost: '))
tip = float(cost) * 0.18
tax = float(cost) * 0.07

def addnumbers (cost, tip, tax):
    return (cost + tip  + tax)

sum = float(cost) + float(tip) + float(tax)
result = ("The sum of {0}, {1} and {2} is {3}".format(cost, tip, tax, sum))

print('Your tip is ', tip)
print('Your tax is ', tax)
print(result)
print("Thank you. See you again!")