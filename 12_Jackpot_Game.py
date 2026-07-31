print("This is a Jackpot game.")
print("You have to choose numbers between 100 to 10000, if you win you will get a prize or if you lose you will get another chance to win.")

while True:
    winning_numbers_1 = 200
    winning_numbers_2 = 600
    winning_numbers_3 = 7000
    winning_numbers_4 = 3000
    winning_numbers_5 = 9999

    try:

        user = int(input("Enter your lucky number here: "))
    
        if user == winning_numbers_1: 
            print("Hey you won boAt earphones.")
        elif user == winning_numbers_2:
            print("Hey you won RTX 3060 graphics card.")
        elif user == winning_numbers_3:
            print("Hey you won Apple's ecosystem")
        elif user == winning_numbers_4:
            print("Hey you won a BMW car.")
        elif user == winning_numbers_5:
            print("You won a Mercedes car.")
        else:
            print("Better luck next time!")
        print("Program Executed successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Program fully executed successfully!")
        print("Have fun!")