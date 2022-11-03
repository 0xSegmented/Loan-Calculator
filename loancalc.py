# Welcome to the loan calculator
print("Welcome to the LoanCalc.")
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # Adding up to compare to
# taking input
first = int(input("Enter when you start\nChoose out of: Jan (1), Feb (2), Mar (3), Apr (4), May (5), Jun (6), Jul (7), Aug (8), Sep (9), Oct (10), Nov (11), Dec (12)\n"))
second = int(input("Enter when you end\n"))
# Calculations
if first in months and second in months:
    if first > second:
        x = first - second
        z = float(input("Enter your monthly pay:\n"))
        total = x * z
        print(total)
    elif second > first:
        x = second - first
        z = float(input("Enter your monthly pay:\n"))
        total = x * z
        print(total)
    else:
        print("broken")
        exit()
        
