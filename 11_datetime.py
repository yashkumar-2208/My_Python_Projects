import datetime

class DateTime():

    def time():

        while True:

            user_input = input("Enter here: ").lower()

            today = datetime.date.today()

            if user_input == "time and date":
                print(datetime.datetime.now())

            elif user_input == "date":
                #print(datetime.date.today()) output: 2026-6-6
                 
                print(datetime.date.today().strftime("%d-%m-%Y"))

            elif user_input == "tomorrow date":
                print("Tomorrow date: ",today + datetime.timedelta(days=1))

            elif user_input == "yesterday date":
                print("Yesterday date: ",today - datetime.timedelta(days=1))
                
            else:
                print("sorry!")

DateTime.time()