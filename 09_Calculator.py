print("A Calculator")

history = []

class Calculator:

    def my_calculator(self):

        try:

            print("A Calculator")
            print("- Press '1' to start the calculation.")
            print("- Press '2' to show the history.")
            print("- Press '3' to clear the history")
            print("- Press '4' to exit the calculator")

            while True: 

                user_input = int(input("Choose your option from (1-4) only!: "))

                if user_input == 1:

                    a = float(input("Enter the first numbers here for calculation: "))
                    b = float(input("Enter the second numbers here for calculation: "))

                    Menubar_2 = ['+', '-', '*', '/', '//','%','**']
                    print(Menubar_2)

                    user_choices = input("Enter your choice: ")

                    if user_choices == "+": 
                        result = (f"The sum is: {a+b}")
                        
                    elif user_choices == "-":
                        result = (f"The difference is: {a-b}")
                        
                    elif user_choices == "*":
                        result = (f"The multiplication is: {a*b}")
                        
                    elif user_choices == "/":
                        if b == 0:
                            result = "Cannot divide by zero!"
                        else:
                            result = f"The division is: {a/b}"
                        
                    elif user_choices == "//":
                        if b == 0:
                            result = "Cannot divide by zero!"
                        else:
                            result = f"The floor division is: {a//b}"
                        
                    elif user_choices == "%":
                        if b == 0:
                            result = "Cannot divide by zero!"
                        else:
                            result = f"The modulus is: {a%b}"
                        
                    elif user_choices == "**":
                        result = (f"The power is: {a**b}")
                        
                    else:
                        result = "Invalid input!"

                    print(result)
                    

                    history.append(f"Your numbers and choices are: {a}{user_choices}{b} \nCalculated result is: {result}")

                elif user_input == 2:

                    if not history:
                        print("You've not done any calculation yet!")

                    else:
                        print("\n--History: --")
                        for item in history:
                            print(item)

                
                elif user_input == 3:
                    if not history:
                        print("You've not stored any history to get cleared!")
                    else:
                        history.clear()
                        print("Your history has been cleared")


                elif user_input == 4:
                    print("Goodbye! Have a wonderful day!")
                    break

                    
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            print("Operation fully executed successfully!")
            

if __name__ == "__main__":
    calculator_system = Calculator()
    calculator_system.my_calculator()