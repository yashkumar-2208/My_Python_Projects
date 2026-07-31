import string
import secrets
import random

class OTP_Generator():

    def otp():

        try:

            a = string.digits
            b = string.ascii_uppercase
            

            digits_part = "".join(random.choices(a,k=4))
            uppercase_part = "".join(random.choices(b,k=4))

            unique_num = digits_part + uppercase_part

            pas_pol = list(unique_num)

            random.shuffle(pas_pol)

            c = ''.join(pas_pol)

            
        
            print("\n🔐 OTP Generation Center")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

            print("1 ➜ Quick OTP")
            print("    Generate a 4-digit verification code.")

            print("\n2 ➜ Secure OTP")
            print("    Generate a 6-digit verification code.")

            print("\n3 ➜ Advanced OTP")
            print("    Generate an alphanumeric verification code.")

            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Select an option (1-3) to continue:")

            while True:

                user_input = int(input("Enter here: "))

                if user_input == 1:

                    otp = ""
                    for i in range(4):
                        otp += secrets.choice(a)
                    print(f"Your generated otp is: {otp}")
                    print("Strength level: Good")


                elif user_input == 2:

                    otp = ""
                    for i in range(6):
                        otp += secrets.choice(a)
                    print(f"Your generated otp is: {otp}")
                    print("Strength level: Strong")
                
                elif user_input == 3:

                    otp = ""
                    for i in range(8):
                        otp += secrets.choice(c)
                    print(f"Your generated otp is: {otp}")
                    print("Strength level: Excellent")
                

                else:
                    print("Choose only between (1-3)")            

        except Exception as e:
            print(f"Error {e}")
            


OTP_Generator.otp()


