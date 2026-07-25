#---- IMPORTS ----#
import qrcode
import time
import validators
import wifi_qrcode_generator.generator
import random
#---- IMPORTS ----#

#------------ IMPORTANT INFO ----------------#
print("Disclaimer & Acceptable Use Policy")
print("""
This QR Code Generator is provided for lawful purposes only. Users are solely responsible for
the content, URLs, text, and information encoded into QR codes generated through this service.
The developer does not endorse, verify, monitor, or take responsibility for user-generated content. 
Any use of this service for unlawful, fraudulent, harmful, misleading, or unauthorized activities is strictly prohibited.
Users must comply with all applicable laws and regulations, including the provisions of the 
Information Technology Act, 2000 (Act No. 21 of 2000) , and other relevant laws of India.
AGE Registration: To use this you must be 18 or 18+.
 """)
#-------------------------------------------#

greetings = ["Nice to meet you", "Welcome","Glad to see you","Move it","Go ahead",
            "Let's start","Move ahead", "Coffee and QR?"]

class QR_Code:

    def qr_code_generate():

        try:

            a = random.choice(greetings)
            print(f"+---- {a} ----+")


            print("""
================= QR Code Generator =================

1.  Generate Website URL QR Code
2.  Generate Text QR Code
3.  Generate Email ID QR Code
4.  Generate Phone Number QR Code
5.  Generate SMS QR Code
6.  Generate WiFi QR Code
7.  Generate Location QR Code
8.  Generate vCard / Contact QR Code
9.  Generate Social Media Profile QR Code
10. UPI OR CODE
11. Exit
                  
=====================================================
""")

            user_choice = int(input("Enter your choice here between (1-10) only! "))

            if user_choice == 1:

                while True:

                    user_data = input("Enter your website url here which you want in your qrcode!: ")

                    if validators.url(user_data):

                        print("Generating your qrcode, (Website URL QR Code) in 1 second")
                        time.sleep(1)

                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                        )
                        qr.add_data(user_data)
                        qr.make(fit=True)
                        img = qr.make_image(fill_color="black", back_color="white")
                        img.show()
                        time.sleep(1)
                        print("QR Code has been generated and shown to the user, if not please try again!")
                        break

                    else:
                        print("Invalid website url!")
                        
                    

            elif user_choice == 2:
                
                user_data = input("Enter your text data here which you want in your qrcode!: ")

                print("Generating your qrcode, text data in 1 second")
                time.sleep(1)

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(user_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.show()
                time.sleep(1)
                print("QR Code has been generated and shown to the user, if not please try again!")

            elif user_choice == 3:

                while True:

                    user_data = input("Enter your email id data which you want in your qrcode!: ")

                    if validators.email(user_data):

                        print("Generating your qrcode, (Email QR Code) in 1 second")
                        time.sleep(1)

                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                        )
                        qr.add_data(user_data)
                        qr.make(fit=True)
                        img = qr.make_image(fill_color="black", back_color="white")
                        img.show()
                        time.sleep(1)
                        print("QR Code has been generated and shown to the user, if not please try again!")
                        break

                    else:
                        print("Invalid Email!")

            elif user_choice == 4:

                while True:

                    user_data = input("Enter your phone number (tip: add your country code like: +91, +7) here which you want in your qrcode!: ")

                    user_data = user_data.replace(" ", "")

                    if user_data.startswith(("+","")) and user_data[1:].isdigit(): 

                        print("Generating your qrcode, (Phone Number QR Code) in 1 second")
                        time.sleep(1)

                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                        )
                        qr.add_data(user_data)
                        qr.make(fit=True)
                        img = qr.make_image(fill_color="black", back_color="white")
                        img.show()
                        time.sleep(1)
                        print("QR Code has been generated and shown to the user, if not please try again!")
                        break

                    else:
                        print("Invalid Phone no!")

            elif user_choice == 5:

                user_data = input("Enter your SMS here which you want in your qrcode!: ")

                print("Generating your qrcode, (SMS QR Code) in 1 second")
                time.sleep(1)

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(user_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.show()
                time.sleep(1)
                print("QR Code has been generated and shown to the user, if not please try again!")

            elif user_choice == 6:

                wifi_name = input("Enter your WiFi name here: ")
                wifi_pass = input("Enter your WiFi password here: ")

                print("Generating your qrcode, (WiFi QR Code) in 1 second")
                time.sleep(1)

                qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
                    ssid=wifi_name ,hidden=False, authentication_type='WPA', password=wifi_pass
                )
                qr_code.print_ascii()
                qr_code.make_image()

                print("QR Code has been generated and shown to the user, if not please try again!")

            elif user_choice == 7:

                user_data = input("Enter your location or GPS Coordinates or Latitude + Longitude here which you want in your qrcode!: ")

                print("Generating your qrcode, location QR Code) in 1 second")
                time.sleep(1)

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(user_data)
                qr.make(fit=True)
                location_url = f"https://maps.google.com/?q={user_data}"

                img = qr.make_image(fill_color="black", back_color="white")
                img = qrcode.make(location_url)

                img.show()
                time.sleep(1)
                print("QR Code has been generated and shown to the user, if not please try again!")


            elif user_choice == 8:
                try:

                    name = input("Enter your name here: ")
                    dob = input("Enter your DOB like (1/1/2000): ")
                    position = input("Enter your designation here: ")
                    address = input("Enter your address here: ")
                    email = input("Enter your email id here: ")
                    number = input("Enter your phone number here without country code: ")
                    number = number.replace(" ", "")
                    number.startswith(("+","")) and number[1:].isdigit()

                    if not validators.email(email):
                        raise ValueError("Invalid email")

                    contact_info = f"""
                        =========================
                    VIRTUAL CARD
                    =========================
                    Name      : {name}   
                    DOB       : {dob}                                
                    Designation  : {position}
                    Address   : {address}
                    Email I'D   : {email}
                    Phone No. : {number}
                    =========================
                                """

                    print("Generating your qrcode, (location QR Code) in 1 second")
                    time.sleep(1)

                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(contact_info)
                    qr.make(fit=True)

                    img = qr.make_image(fill_color="black", back_color="white")

                    img.show()
                    time.sleep(1)
                    

                except Exception as e:
                    print(e)

                finally:
                    print("QR Code has been generated and shown to the user, if not please try again!")


            elif user_choice == 9:

                user_data = input("Enter your profile/Portfolio url here which you want in your qrcode!: ")

                if validators.url(user_data):

                    print("Generating your qrcode, (Profile/Portfolio URL QR Code) in 1 second")
                    time.sleep(1)

                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(user_data)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color="black", back_color="white")
                    img.show()
                    time.sleep(1)
                    print("QR Code has been generated and shown to the user, if not please try again!")

                else:
                    print("Invalid url!")

            elif user_choice == 10:

                name = input("Enter your real and valid name here: ")
                main = input("Enter your real and valid upi id or phone no: ")

                print("Generating your qrcode, location QR Code) in 1 second")
                time.sleep(1)

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                
                qr.make(fit=True)
                payment_url = f"upi://pay?pa={main}k&pn={name}"

                img = qr.make_image(fill_color="black", back_color="white")
                img = qrcode.make(payment_url)

                img.show()
                time.sleep(1)
                print("QR Code has been generated and shown to the user, if not please try again!")
                
                

            elif user_choice == 11:
                print("Goodbye! have a wonderful day!")
                
            else:
                print("Please enter between (1-10) 0nly")

        except Exception as e:
            print(f"Error {e}")

        finally:
            print("Program executed successfully!")

QR_Code.qr_code_generate()