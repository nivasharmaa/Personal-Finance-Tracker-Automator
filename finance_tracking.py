import csv
import json
import os

def sum_expenses_for_month(csv_file_path):
    total_expenses = 0.0
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        #skip the first three lines
        next(reader)
        for row in reader:
            #check if the row corresponds to the given month and year, and is a debit transaction
            date, merchant_name, account, category_name, amount = row
            amount = amount.replace(',', '')
            if amount.lower() == 'debit':
                total_expenses += float(amount)
    return total_expenses
            
#The purpose of this function is to extract all the debit transactions from the csv file and add it to one variable total_expenses.
def update_expenses_json(json_file_path, month, total_expenses):
    expenses_data = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            expenses_data = json.load(json_file)
# If this file doesn't exist we are gonna have an empty expenses data object
    expenses_data[month] = total_expenses 

    with open(json_file_path, 'w') as json_file:
        json.dump(expenses_data, json_file, indent=4)

month_input = input("Please enter the month (format: YYYY-MM): ") 

csv_file_name = 'Transactions.csv' #input file
json_file_name = "monthly_expenses.json"  #outputfile
total_month_expenses = sum_expenses_for_month(csv_file_name)
print("Total expenses for {month_input}: {total_month_expenses}")


update_expenses_json(json_file_name, month_input, total_month_expenses)

    