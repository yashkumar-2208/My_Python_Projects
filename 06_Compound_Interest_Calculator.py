print("This is a compound interest calculator, Hence can make mistake!")

class Compound_Interest_Calculator():

    def compund_calculator():

        while True:

            try:

                principle = float(input("Enter total amount here: "))
                if principle > 0:
                    print(f"You have entered ${principle} amount.")
                else:
                    print("Enter a valid amount!")
                    continue

                rate_of_interest = float(input("Enter total rate of interest here: "))
                    
                if rate_of_interest > 0:
                    print(f"You have entered {rate_of_interest}% rate of interest.")
                else:
                    print("Enter a valid rate of interest!")
                    continue

                time_period = int(input("Enter total time period in years here: "))
                           
                if time_period > 0: 
                    print(f"You have entered {time_period} year/s")
                else:
                    print("Enter valid time period!")
                    continue

                total = principle * pow((1 + rate_of_interest / 100), time_period)
                print(f"Your total balance after calculation of \n Total years: {time_period} year/s \n Total rate of interest: {rate_of_interest}% \n total amount: {principle} \n Total value: {total:.2f} \n Interest earned: {total - principle}")
            
            except Exception as e:
                (f"Error: {e}")


Compound_Interest_Calculator.compund_calculator()