import csv, datetime
from .utils import FILE_PATH, exist_file


def write_csv(description, amount, category, date):
    
    if date:
        date_now = date
    else:
        date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    

    if not exist_file:
        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=['id','description','amount','date','category'])
            writer.writeheader()
            writer.writerow({'id':'1', 'description': description, 'amount': amount, 'date': date_now, 'category': category})
            print("Expense added successfully (ID: 1)")
            return
        
    if exist_file:

        with open(FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            current_id = str(len(rows) + 1)

        with open(FILE_PATH, 'a', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=['id','description','amount','date', 'category'])
            writer.writerow({'id': current_id, 'description':description, 'amount':amount, 'date': date_now, 'category': category})
            print(f"Expense added successfully (ID: {current_id})")
            return