import csv
from .utils import FILE_PATH, exist_file

def delete_expense(expense_id):

    if not exist_file:
        print("No CSV file found.")
        return
    
    if exist_file:

        try:
            with open(FILE_PATH, 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                rows = list(reader)
                if not (0 < expense_id <= len(rows)):
                    print("ID is not register")
                    return
                else:
                    filtered_rows = list()
                    for row in rows:
                        if int(row['id']) != expense_id:
                            filtered_rows.append(row)

                    with open(FILE_PATH, 'w', newline='') as file:
                        writer = csv.DictWriter(file,
                                                delimiter=',',
                                                fieldnames=['id','description','amount','date','category'])
                        writer.writeheader()
                        i = 0
                        for row in filtered_rows:
                            i += 1
                            writer.writerow({'id': i,
                                            'description': row['description'],
                                            'amount': row['amount'],
                                            'date': row['date'],
                                            'category': row['category']})
                
                print("Expense deleted successfully")
                return
            
        except Exception as e:
            print(e)
            