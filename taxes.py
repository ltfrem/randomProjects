#get user input
income = int(input('What is your income?\n'))
retirement_pct = int(input('What percent will you put towards retirement?\n'))
retirement_pct = retirement_pct / 100
#retirement_pct = 0.00
retirement_amt = income * retirement_pct
adj_income = income - retirement_amt
##print("Income with retirement taken out:", str(adj_income))

##calculate tax rate based on post-retirement adjusted income
print("This program assumes you are married & filing jointly for 2023.")
if adj_income <= 22000:
    tax_pct = 0.1
elif adj_income >= 22001 and adj_income <= 89450:
    tax_pct = 0.12
elif adj_income >= 89450 and adj_income <= 190750:
    tax_pct = 0.22
elif adj_income >= 190751 and adj_income <= 364200:
    tax_pct = 0.24
elif adj_income >= 364201 and adj_income <= 462500:
    tax_pct = 0.32
elif adj_income >= 462501 and adj_income <= 693750:
    tax_pct = 0.35
else:
    tax_pct = 0.37

if tax_pct == 0.1:
    total_tax_bill = adj_income * tax_pct
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))
elif tax_pct == 0.12:
    total_tax_bill = 2200 + ((adj_income - 22000) * tax_pct)
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))
elif tax_pct == 0.22:
    total_tax_bill = 10294 + ((adj_income - 89450) * tax_pct)
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))
elif tax_pct == 0.24:
    total_tax_bill = 32580 + ((adj_income - 32580) * tax_pct)
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))
elif tax_pct == 0.32:
    total_tax_bill = 74208 + ((adj_income - 74208) * tax_pct)
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))
elif tax_pct == 0.35:
    total_tax_bill = 105664 + ((adj_income - 105664) * tax_pct)
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))
else:
    total_tax_bill = 386601.50 + ((adj_income - 186601.50) * tax_pct)
    print("Taxes:", str(total_tax_bill), "...Retirement:", str(retirement_amt), "...Income:", str(adj_income - total_tax_bill))