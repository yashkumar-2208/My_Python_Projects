import requests
import random
greetings = ["Nice to meet you", "Welcome","Glad to see you","Do It","Go ahead",
            "Let's start","Move ahead", "Coffee and Currency?"]

class Currency_Convertor:
    
    def convert_currency(self):
        a = random.choice(greetings)
        print(f"\n+---- {a} ----+")

        print("\n+------------------- Must write like --------------------+")
        print("INR, USD, EUR, GBP, JPY, AUD, CAD, More. Only 3 Capital Letters. ")
        print("The prices may vary according to the market.")
        print("+--------------------------------------------------------+")

        while True:

            try:

                

                from_currency = input("Enter the currency here: ").upper()
                to_currency = input("Enter the currency here: ").upper()
                amount = float(input("Enter amount here: "))

                url = "https://api.frankfurter.dev/v1/latest"
                params = {"from": from_currency, "to": to_currency}
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                rate = data["rates"][to_currency]
                result = amount * rate

                print()
                print("┌─────────────────────────────────────────┐")
                print("│           CURRENCY CONVERTER            │")
                print("│                                         │")
                print(f"│  Amount: {amount:<31}│")
                print("│                                         │")
                print(f"│  From:   {from_currency:<31}│")
                print(f"│  To:     {to_currency:<31}│")
                print("│                                         │")
                print("│              [CONVERTED]                │")
                print("│                                         │")
                print(f"│  {amount:.2f} {from_currency} = {result:.2f} {to_currency:<20}│")
                print("└─────────────────────────────────────────┘")
                print()
                break

            except requests.exceptions.HTTPError:
                print("\nInvalid currency code or conversion not available.")

            except requests.exceptions.RequestException:
                print("\nNetwork error. Please check your internet connection.")

            except ValueError:
                print("\nPlease enter a valid amount.")


if __name__ == "__main__":
    systm = Currency_Convertor()
    systm.convert_currency()