class Unit_Convertor():

    @staticmethod
    def unit_conversion():
        
        print(f"\n-- Menu bar --\n")
        print("Press '1' for length conversion")
        print("Press '2' for mass/weight conversion")
        print("Press '3' for time conversion")
        print("Press '4' for area conversion")
        print("Press '5' for volume conversion")
        print("press '6' for speed conversion")
        print("Press '7' for data storage conversion")
        print("Press '8' for energy conversion")
        print("Press '9' for pressure conversion")
        print("Press '10' for temperature conversion ")
        print("Press '11' to exit the program")
        print("             --")


        try:

            while True:

                user_input = int((input("Enter your 'Menu Bar' number here: ")))

                if user_input == 1:
                    print("You have chosen length conversion!")
                    
                    print("Choose a conversion option by entering its number:")
                    print("""
1. Meter → Centimeter                   14. Inch → Foot
2. Meter → Kilometer                    15. Yard → Meter
3. Kilometer → Meter                    16. Meter → Yard
4. Inch → Centimeter                    17. Yard → Foot
5. Foot → Meter                         18. Foot → Yard
6. Meter → Foot                         19. Mile → Meter
7. Mile → Kilometer                     20. Meter → Mile
8. Centimeter → Meter                   21. Kilometer → Mile
9. Kilometer → Centimeter               22. Millimeter → Meter
10. Centimeter → Kilometer              23. Meter → Millimeter
11. Inch → Meter                        24. Centimeter → Inch
12. Meter → Inch                        25. Kilometer → Foot
13. Foot → Inch                         26. Foot → Kilometer

If you want to change Menu Bar option press 0""")
                    
                    user_choice = int((input("Enter length conversion number here: ")))


                    if user_choice == 0:
                        continue

                    units = float(input("Enter the value which you wants to convert: "))
                    

                    if user_choice == 1:
                        print(f"You've chose {user_choice}")
                        print(f"Your converted value is: {units * 100}cm")

                    elif user_choice == 2:
                        print(f"You have chosen {user_choice}")
                        print(f"Your converted value is: {units / 1000}km")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}m")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2.54}cm")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.3048}m")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.28084}ft")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.60934}km")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 100}m")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 100000}cm")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 100000}km")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.0254}m")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.0254}in")


                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 12}in")


                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 12}ft")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.9144}m")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.9144}yd")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3}ft")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3}yd")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1609.34}m")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1609.34}mi")

                    elif user_choice == 21:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1.60934}mi")

                    elif user_choice == 22:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000}m")

                    elif user_choice == 23:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}mm")

                    elif user_choice == 24:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 2.54}in")

                    elif user_choice == 25:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3280.84}ft")

                    elif user_choice == 26:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3280.84}km")
                    
                    else:
                        print("Choose between (1 to 26) only!")


                elif user_input == 2:
                    print("You've chosen mass/weight conversion")
                    print("Choose a conversion option by entering its number:")
                    print("""                           
1.  Kilogram → Gram                 11. Gram → Milligram
2.  Gram → Kilogram                 12. Milligram → Gram
3.  Pound → Kilogram                13. Ounce → Gram
4.  Kilogram → Pound                14. Gram → Ounce
5.  Ton → Kilogram                  15. Ounce → Pound
6.  Kilogram → Ton                  16. Pound → Ounce
7.  Gram → Pound                    17. Ton → Pound
8.  Pound → Gram                    18. Pound → Ton
9.  Kilogram → Milligram            19. Ton → Gram
10. Milligram → Kilogram            20. Gram → Ton
\n If you wants to go back then enter 0""" )

                                                                      

                    user_choice = int((input("Enter Mass/Weight conversion number here: ")))

                    if user_choice == 0:
                        continue

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units *1000}g")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units/1000}kg")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.453592}kg")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2.20462}lb")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}kg")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000}t")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 453.592}t")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 453.592}g")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000000}mg")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000000}kg")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}mg")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000}g")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 28.3495}g")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 28.3495}oz")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 16}lb")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 16}oz")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2204.62}lb")
                    
                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 2204.62}t")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000000}g")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000000}t")

                    else:
                        print("Choose number between (1 to 20) only")

                elif user_input == 3:
                    print("You've chosen Time conversion")
                    print("Choose a conversion option by entering its number:")
                    print("""                           

1.  Minute → Second                11. Week → Hour
2.  Hour → Minute                  12. Month → Day
3.  Day → Hour                     13. Month → Week
4.  Week → Day                     14. Year → Month
5.  Year → Day                     15. Year → Week
6.  Second → Minute                16. Year → Hour
7.  Minute → Hour                  17. Year → Minute
8.  Hour → Second                  18. Year → Second
9.  Day → Minute                   19. Hour → Day
10. Day → Second                   20. Minute → Day
\n If you wants to go back then enter 0 
""")

                    user_choice = int((input("Enter Time conversion number here: ")))

                    if user_choice == 0:
                        continue

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 60}sec")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 60}min")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 24}hr")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 7}day")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 365}day")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 60}min")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 60}hr")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3600}sec")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1440}min")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 86400}sec")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 168}hr")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 30}day")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 4.345}week")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 12}mo")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 52.143}week")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 8760}hr")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 525600}min")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 31536000}sec")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 24}day")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1440}day")

                    elif user_choice < 20:
                        print("Choose number between (1 to 20) only")

                    else:
                        print("Choose number between (1 to 20) only")


                elif user_input == 4:
                    print("You've chosen Area conversion")
                    print("Given below are the available conversion operation")
                    print("""
1.  m² → cm²                      11. ft² → m²
2.  km² → m²                      12. m² → ft²
3.  Acre → m²                     13. yd² → m²
4.  Hectare → m²                  14. m² → yd²
5.  cm² → m²                      15. cm² → km²
6.  m² → km²                      16. km² → cm²
7.  m² → Acre                     17. Acre → ft²
8.  m² → Hectare                  18. ft² → Acre
9.  Hectare → Acre                19. Hectare → km²
10. Acre → Hectare                20. km² → Hectare
\n If you wants to go back then enter 0 
""")

                    user_choice = int((input("Enter Area conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 10000}cm²")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000000}m²")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 4046.86}m²")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 10000}m²")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 10000}m²")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000000}km²")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 4046.86}Acre")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 10000}Hectare")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2.47105}Acre")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 2.47105}Hectare")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.092903}m²")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.092903}ft²")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.836127}m²")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.836127}yd²")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 10000000000}km²")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 10000000000}cm²")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 43560}ft²")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 43560}Acre")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 100}km²")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 100}Hectare")

                    
                    else:
                        print("Choose number between (1 to 20) only!")

                elif user_input == 5:
                    print("You've chosen Volume Conversion")
                    print("""
Given below are the available Volume Conversion operations

1.  Liter → Milliliter                11. Cubic Foot → Liter
2.  Milliliter → Liter                12. Liter → Cubic Foot
3.  Cubic Meter → Liter               13. Cubic Inch → Milliliter
4.  Liter → Cubic Meter               14. Milliliter → Cubic Inch
5.  Gallon (US) → Liter               15. Pint (US) → Liter
6.  Liter → Gallon (US)               16. Liter → Pint (US)
7.  Cubic Centimeter → Milliliter     17. Quart (US) → Liter
8.  Milliliter → Cubic Centimeter     18. Liter → Quart (US)
9.  Cubic Yard → Cubic Meter          19. Fluid Ounce → Milliliter
10. Cubic Meter → Cubic Yard          20. Milliliter → Fluid Ounce

""")
                    user_choice = int((input("Enter Volume conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))


                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}ml")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000}l")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}l")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000}m³")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.78541}l")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3.78541}gal")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units}ml")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units}cm³")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.764555}m³")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.764555}yd³")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 28.3168}l")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 28.3168}ft³")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 16.3871}ml")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 16.3871}in³")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.473176}l")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.473176}pt")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units *  0.946353}l")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.946353}qt")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 29.5735}ml")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 29.5735}fl")



                    else:
                        print("Choose number between (1 to 20) only!")


                elif user_input == 6:
                    print("""
You've chosen Speed Conversion
Given below are the available conversion operations

1.  km/h → m/s                 11. Knot → km/h
2.  m/s → km/h                 12. km/h → Knot
3.  mph → km/h                 13. Knot → mph
4.  km/h → mph                 14. mph → Knot
5.  m/s → mph                  15. ft/s → m/s
6.  mph → m/s                  16. m/s → ft/s
7.  km/h → ft/s                17. Mach → km/h
8.  ft/s → km/h                18. km/h → Mach
9.  m/s → Knot                 19. Mach → mph
10. Knot → m/s                 20. mph → Mach

""")

                    user_choice = int((input("Enter Speed conversion number here (1-20): ")))

                    units = float(input("Enter the value which you wants to convert: "))


                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3.6}m/s")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3.6}km/h")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.60934}km/h")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1.60934}mph")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 2.23694}mph")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 2.23694}m/s")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.911344}ft/s")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.911344}km/h")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.94384}knot")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1.94384}m/s")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.852}km/h")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1.852}knot")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.15078}mph")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1.15078}knot")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.3048}m/s")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.3048}ft/s")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1234.8}km/h")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1234.8}Mach")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 767.269}mph")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 767.269}Mach")

                    else:
                        print("Choose number between (1 to 20) only!")
                    

                elif user_input == 7:
                    print("""
You've chosen Data Storage Conversion
Given below are the available conversion operations

1.  Byte → Bit                  11. Byte → KB
2.  KB → Byte                   12. KB → MB
3.  MB → KB                     13. MB → GB
4.  GB → MB                     14. GB → TB
5.  TB → GB                     15. Bit → Byte
6.  Byte → MB                   16. KB → Bit
7.  MB → Byte                   17. MB → Bit
8.  GB → KB                     18. GB → Bit
9.  TB → MB                     19. TB → Bit
10. TB → KB                     20. Bit → KB

If you want to go back then enter 0
""")

                    user_choice = int((input("Enter Speed conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))


                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 8}bit")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}B")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}KB")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}MB")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024}GB")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1048576}MB")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1048576}Byte")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1048576}KB")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1048576}MB")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1073741824}KB")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1024}KB")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1024}MB")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1024}GB")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1024}TB")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 8}Byte")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1024 * 8}Bit")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1048576 * 8}Bit")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1073741824 * 8}Bit")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1099511627776 * 8}Bit")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / (1024 * 8)}KB")

                    else:
                        print("Choose number between (1 to 20) only!")


                elif user_input == 8:
                    print("""
You've chosen Energy Conversion
Given below are the available conversion operations

1.  Calorie → Joule           11. Joule → kWh
2.  Joule → Calorie           12. Calorie → kWh
3.  kWh → Joule               13. kWh → Calorie
4.  Joule → kWh               14. BTU → Joule
5.  kWh → Calorie             15. Joule → BTU
6.  Calorie → kWh             16. BTU → Calorie
7.  kJ → Joule                17. Calorie → BTU
8.  Joule → kJ                18. kWh → BTU
9.  kJ → Calorie              19. BTU → kWh
10. Calorie → kJ              20. kJ → kWh

If you want to go back then enter 0
""")

                    user_choice = int((input("Enter Energy conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 4.184}J")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 4.184}cal")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3600000}J")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3600000}kWh")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 860420.65}Calorie")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 860420.65}kWh")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}J")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000 }kJ")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 239.006}Calorie")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units  / 239.006}kJ")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3600000}kWh")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 860420.65}kWh")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 860420.65}Calorie")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1055.06}J")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1055.06}BTU")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 252.164}Calorie")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 252.164}BTU")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 3412.14}BTU")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3412.14}kWh")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 3600}kWh")

                    else:
                        print("Choose number between (1 to 20) only")

                elif user_input == 9:
                    print("""
You've chosen Pressure Conversion
Given below are the available conversion operations

1.  atm → Pascal               11. Pascal → atm
2.  bar → Pascal               12. Pascal → bar
3.  psi → Pascal               13. Pascal → psi
4.  Pascal → mmHg              14. mmHg → Pascal
5.  atm → bar                  15. bar → atm
6.  atm → psi                  16. psi → atm
7.  bar → psi                  17. psi → bar
8.  mmHg → atm                 18. atm → mmHg
9.  mmHg → bar                 19. bar → mmHg
10. kPa → Pascal               20. Pascal → kPa

If you want to go back then enter 0
""")

                    user_choice = int((input("Enter Energy conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 101325}Pa")

                    elif user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 100000}Pa")

                    elif user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 6894.76}Pa")

                    elif user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 133.322}mmHg")

                    elif user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1.01325}bar")

                    elif user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 14.6959}psi")

                    elif user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 14.5038}psi")

                    elif user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 760}atm")

                    elif user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 750.062}bar")

                    elif user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 1000}Pa")

                    elif user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 101325}atm")

                    elif user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 100000}bar")

                    elif user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 6894.76}psi")

                    elif user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 133.322}Pa")

                    elif user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1.01325}atm")

                    elif user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 14.6959}atm")

                    elif user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 14.5038}bar")

                    elif user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 760}mmHg")

                    elif user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 750.062}mmHg")

                    elif user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 1000 }kPa")

                    else:
                        print("Choose number between (1 to 20) only!")

                elif user_input == 10:


                    print("""
You've chosen Temperature Conversion
Given below are the available conversion operations

1.  Celsius → Fahrenheit          11. Rankine → Celsius
2.  Fahrenheit → Celsius          12. Celsius → Rankine
3.  Celsius → Kelvin              13. Rankine → Fahrenheit
4.  Kelvin → Celsius              14. Fahrenheit → Rankine
5.  Fahrenheit → Kelvin           15. Kelvin → Rankine
6.  Kelvin → Fahrenheit           16. Rankine → Kelvin
7.  Celsius → Réaumur             17. Réaumur → Fahrenheit
8.  Réaumur → Celsius             18. Fahrenheit → Réaumur
9.  Kelvin → Réaumur              19. Kelvin → Delisle
10. Réaumur → Kelvin              20. Delisle → Kelvin

If you want to go back then enter 0
""")
                          
                    user_choice = int((input("Enter Energy conversion number here: ")))

                    units = float(input("Enter the value which you wants to convert: "))

                    if user_choice == 1:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units * 9/5)+32}°F")

                    if user_choice == 2:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units - 32)*5/9}°C")

                    if user_choice == 3:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units + 273.15 }K")

                    if user_choice == 4:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units - 273.15}°C")

                    if user_choice == 5:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units - 32) * 5/9 + 273.15}K")

                    if user_choice == 6:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units - 273.15) * 9/5 + 32}°F")

                    if user_choice == 7:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 0.8}°Re")

                    if user_choice == 8:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units / 0.8}°C")

                    if user_choice == 9:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units - 273.15) * 0.8}°Re")

                    if user_choice == 10:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units / 0.8) + 273.15}K")

                    if user_choice == 11:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units - 491.67) * 5/9}°C")

                    if user_choice == 12:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units + 273.15) * 9/5}°R")

                    if user_choice == 13:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units - 459.67}°F")

                    if user_choice == 14:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units + 459.67}°R")

                    if user_choice == 15:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 9/5}°R")

                    if user_choice == 16:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {units * 5/9}K")

                    if user_choice == 17:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(units / 0.8) * 9/5 + 32}°F")

                    if user_choice == 18:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {((units - 32) * 5/9) * 0.8}°Re")

                    if user_choice == 19:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {(373.15 - units) * 3/2}°De")

                    if user_choice == 20:
                        print(f"You've chosen: {user_choice}")
                        print(f"Your converted value is: {373.15 - (units * 2/3)}K")

                elif user_input == 11:
                    print("Goodbye!")
                    break

                else:
                    print("Enter available operation")

                print("Operation executed successfully!")


        except Exception as e:
            print(f"Error: {e}")

        finally:
            print("Program fully executed successfully!")
    

Unit_Convertor.unit_conversion()
