import csv
from .utils import FILE_PATH, exist_file
import datetime

def summary_expenses():

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
        
        total_sum = 0
        for row in rows:
            total_sum += int(row['amount'])
        
        print(f"Total expenses: ${total_sum}")

    except Exception as e:
        print(f"Error reading file: {e}")


def summary_per_month(month):

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
        
        total_sum_per_month = 0
        for row in rows:
            date = row['date']
            date_month = date.split("-")[1]
            if int(date_month) == int(month):
                total_sum_per_month += int(row['amount'])

        name_month = (datetime.datetime.strptime(str(month), "%m")).strftime("%B")     
        
        print(f"Total expenses for {name_month}: ${total_sum_per_month}")

    except Exception as e:
        print(f"Error reading file: {e}")
