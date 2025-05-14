balance = 50
item = 15
tax_rate  = .03
tax = item * tax_rate
total = item + tax

balance -= total

print("Your opening balance was $50")
print(f"The item (${item}) + tax (${tax}) = ${total}")
print(f"Your remaning balance is ${balance}")