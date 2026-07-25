import random

print("\n+---- This is a Rock, Paper, Scissors Game! ----+\n")

class Game:

    def gaming(self):
        print("You have given three choices you have to choose one at once. Choices are:\n - Rock\n - Paper \n - Scissors \n - exit/quit to Exit the game")

        choices = ["Paper", "Rock", "Scissors"]


        while True: 
            try: 

                computer = random.choice(choices)
                user = input("Enter your choice here: ").capitalize()

                try:
                    user =  user.replace(" ","")
                    if user in ["Rock", "Paper", "Scissors"]:

                        if user == "Rock" and computer == "Rock":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("It's a tie!")

                        elif user == "Paper" and computer == "Scissors":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("Computer won!")

                        elif user in ["Scissors","Scisors"] and computer == "Paper":
                            print(f"You have chosen {user} and the computer has chosen {computer}")
                            print("You won!")

                        elif user == "Rock" and computer == "Paper":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("Computer won!")

                        elif user == "Paper" and computer == "Paper":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("It's a tie!")

                        elif user in ["Scissors","Scisors"] and computer == "Rock":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("Computer won!")

                        elif user in ["Scissors","Scisors"] and computer == "Scissors":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("It's a tie!")

                        elif user == "Paper" and computer == "Rock":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("You won!")

                        elif user == "Rock" and computer == "Scissors":
                            print(f"You have chosen {user} and computer has chosen {computer}")
                            print("You won!")

                        play_again = input("Play again? (y/n): ").strip().lower()
                        if play_again == "n":
                            print("Thanks for playing! Goodbye!")
                            break
                        elif play_again == "y":
                            print("Great! Let's play again.\n")

                    elif user in ["quit","exit", "Quit", "Exit"]:
                        print("Game Over!")
                        break

                    else:
                        print("Choose only from (Rock / Paper / Scissors)")

                except Exception as e:
                    print("Invalid input!")

            except Exception as e:
                print("Error occurred in the system")

            finally:
                print("Game executed successfully!")

if __name__ == "__main__":
    game_system = Game()
    game_system.gaming()