import csv
from .utils import FILE_PATH, exist_file
from tabulate import tabulate

def list_expenses():

    if not exist_file:
        print("No CSV file found.")
        return

    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            rows = list(reader)

        if not rows:
            print("No hay registros.")
            return

        table = [[row['id'], row['date'], row['description'], row['category'], f"${row['amount']}"] for row in rows]
        print(tabulate(table, headers=["ID", "Date", "Description", "Category", "Amount"], tablefmt="heavy-grid"))

    except Exception as e:
        print(f"Error reading file: {e}")


def list_expenses_for_category(category):

    if not exist_file:
        print("No CSV file found.")
        return
    
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            rows = list(reader)

        if not rows:
            print("There are no records.")
            return

        table = [[row['id'], row['date'], row['description'], row['category'], f"${row['amount']}"] for row in rows if row['category'].lower() == category.lower()]
        print(tabulate(table, headers=["ID", "Date", "Description", "Category", "Amount"], tablefmt="heavy-grid"))

    except Exception as e:
        print(f"Error reading file: {e}")