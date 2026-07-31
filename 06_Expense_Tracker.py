class Expense_Tracker:


    def __init__(self):
        self.store_expenses = []

    def add_expenses(self):

        name = input("Enter the item name here: ")
        amount = float(input("Enter the amount of the item: "))
        category = input("Enter the category here: ")

        categories = {
            "name":name,
            "amount":amount,
            "category":category
        }

        self.store_expenses.append(categories)

    def view_expense(self):

        if len(self.store_expenses) == 0:
            print("No expenses found!")

        for expense in self.store_expenses:
            print(f"Item: {expense['name']}")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")

    def total_expense_amount(self):

        total = 0

        for expense in self.store_expenses:
            total += expense["amount"]

        print(f"Total expense: {total:.2f}")

    def menu(self):

        while True:

            try: 

            
                print("\n+--------------------------------+")
                print("|        EXPENSE TRACKER         |")
                print("+--------------------------------+")
                print("| 1. Add Expense                |")
                print("| 2. View Expenses              |")
                print("| 3. Total Expense              |")
                print("| 4. Exit                       |")
                print("+--------------------------------+")

                
                user_choices = int(input("Enter your choice from 1-4 here: "))

                if user_choices == 1:
                    self.add_expenses()

                elif user_choices == 2:
                    self.view_expense()

                elif user_choices == 3:
                    self.total_expense_amount()

                else:
                    print("Enter from only 1-4! ")

            except ValueError:
                print("\nPlease enter a valid number!")


            finally:
                print("Program executed successfully! ")


if __name__ == "__main__":
    exp_system = Expense_Tracker()
    exp_system.menu()