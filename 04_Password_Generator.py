import secrets
import string
import random

class Password_generator:

    def secured_password(self):

        a = string.ascii_lowercase
        b = string.ascii_uppercase
        c = string.digits
        d = string.punctuation
        all_combined = a+b+c+d 
    
        
        pas_pol = list((all_combined))

        random.shuffle(pas_pol)

        unique_password = ''.join(pas_pol)


        print("""
╔══════════════════════════════════════════════╗
║          SECURE PASSWORD GENERATOR           ║
╚══════════════════════════════════════════════╝

Choose an option:

1. Lowercase Password (a-z)
2. Uppercase Password (A-Z)
3. Numeric Password (0-9)
4. Special Character Password (!@#$...)
5. Mixed Password (Letters + Numbers + Symbols)
6. Recommended Secure Password ⭐
7. Enter exit or quit to exit from the Password Generator

Note:
• The recommended option provides maximum security.
• Type 'show password' to view your last generated password.
""")
        
   
        try:

            stored_password = None
    

            while True: 
                user_input = input("Enter your choice here between (1 to 7): ")
       
                if user_input == "1":


                    user_choice = int(input("Enter the number that you need the password length: "))

                    if user_choice < 8:
                        print("The value must be greater than 8.")
                    
                    
                    elif user_choice >= 8:
                        password = ""
                        for i in range(user_choice):
                            password += secrets.choice(a)
                        print(f"Your secured password is: {password}")
                        print("Strength level: Weak")
                        stored_password = password

                    else:
                        print("Sorry")
                        
        
                elif user_input == "2":

                    user_choice = int(input("Enter the number that you need the password length: "))

                    if user_choice < 8:
                        print("The value must be greater than 8.")
                        

                    else:
                        password = ""
                        for i in range(user_choice):
                            password += secrets.choice(b)
                        print(f"Your secured password is: {password}")
                        print("Strength level: Weak")
                        stored_password = password

                elif user_input == "3":

                    user_choice = int(input("Enter the number that you need the password length: "))

                    if user_choice < 8:
                        print("The value must be greater than 8.")

                    else:
                        password = ""
                        for i in range(user_choice):
                            password += secrets.choice(c)
                        print(f"Your secured password is: {password}")
                        print("Strength level: Weak")
                        stored_password = password

                elif user_input == "4":
                    user_choice = int(input("Enter the number that you need the password length: "))

                    if user_choice < 8:
                        print("The value must be greater than 8.")

                    else:
                        password = ""
                        for i in range(user_choice):
                            password += secrets.choice(d)
                        print(f"Your secured password is: {password}")
                        print("Strength level: Weak")
                        stored_password = password

                elif user_input == "5":
                    user_choice = int(input("Enter the number that you need the password length: "))

                    if user_choice < 8:
                        print("The value must be greater than 8.")
                        continue

                    elif user_choice >= 8 and user_choice <=11:
                        strength = "Good"

                    elif user_choice >= 12 and user_choice <= 15:
                        strength = "Strong"

                    else:
                        strength = "Excellent"

                    password = ""
                    for i in range(user_choice):
                        password += secrets.choice(all_combined)
                    print(f"Your secured password is: {password}")
                    print(f"Strength level: {strength}")
                    stored_password = password

                elif user_input == "6":
                    password = ""
                    for i in range(20):
                        password += secrets.choice(unique_password)
                    print(f"Your secured password is: {password}")
                    print("Strength level: Powerful")
                    stored_password = password

                elif user_input == "7":
                    print("Goodbye! ")
                    break

                elif user_input in ["show pass", "show password","Show pass","Show password",
                                    "show pas", "sho pass", "sho pas","sho password","stored pass",
                                    "stored password","Stored password","Saved pass","Saved password"]:
                    if stored_password:
                        print(f"Your stored password is: {stored_password}")
                        print("After closing the app you will not able to see your stored password again!")

                          
                    else:
                        print("You have not stored any password yet!")


                else:
                    print("Choose only between (1 - 7)!")
                    continue
                         

        except Exception as e:
            print(f"Error {e}")

        finally:
            print("Program fully executed successfully!")


if __name__ == "__main__":
    password_system = Password_generator()
    password_system.secured_password()