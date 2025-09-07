
# Andrea Aguirre
# X00208680
week_pay = 0
week_pay_due = 0
bonus = 0
NUMBER_DAYS = 7
total_pay = 0

print("***************************")
print("*       GiftsToGo         *")
print("***************************")
print("* 1) Process Employee Pay *")
print("* 2) Company Statistics   *")
print("* 3) Generate Password    *")
print("* 4) Exit                 *")
print("***************************")
user_choice = int(input("Please select menu option:"))
while user_choice != 4:
    if user_choice == 1:
        print("************************")
        print("* Process Employee Pay *")
        print("************************")
        employee_name = str(input("Enter employee name:"))
        days_worked = int(input("How many days did the employee work:"))
        if days_worked == 1:
           for number in range (1):
             pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
             total_pay += pay
             week_pay_due = total_pay * NUMBER_DAYS

             days_worked += 7

             if pay <= 50:
                 week_pay = week_pay_due / 0.04
                 print(employee_name, "received a bonus of",week_pay)
             elif pay >= 50:
                week_pay += week_pay
                print(employee_name, "did not receive a bonus")



           print("Basic Weekly Pay Due:", week_pay_due)
           print(employee_name, "Worked" , days_worked , "this week")
           print(employee_name, "received total weekly play of", week_pay)

        elif days_worked == 2:
            for number in range(2):
                pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
                total_pay += pay
                week_pay_due = total_pay * NUMBER_DAYS

                days_worked += 7

                if pay <= 50:
                    week_pay = week_pay_due / 0.04
                    print(employee_name, "received a bonus of", week_pay)
                elif pay >= 50:
                    week_pay += week_pay
                print(employee_name, "did not receive a bonus")

            print("Basic Weekly Pay Due:", week_pay_due)
            print(employee_name, "Worked", days_worked, "this week")
            print(employee_name, "received total weekly play of", week_pay)

        elif days_worked == 3:
            for number in range(3):
                pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
                total_pay += pay
                week_pay_due = total_pay * NUMBER_DAYS

                days_worked += 7

                if pay <= 50:
                    week_pay = week_pay_due / 0.04
                    print(employee_name, "received a bonus of", week_pay)
                elif pay >= 50:
                    week_pay += week_pay
                print(employee_name, "did not receive a bonus")

            print("Basic Weekly Pay Due:", week_pay_due)
            print(employee_name, "Worked", days_worked, "this week")
            print(employee_name, "received total weekly play of", week_pay)

        elif days_worked == 4:
            for number in range(4):
                pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
                total_pay += pay
                week_pay_due = total_pay * NUMBER_DAYS

                days_worked += 7

                if pay <= 50:
                    week_pay = week_pay_due / 0.04
                    print(employee_name, "received a bonus of", week_pay)
                elif pay >= 50:
                    week_pay += week_pay
                print(employee_name, "did not receive a bonus")

            print("Basic Weekly Pay Due:", week_pay_due)
            print(employee_name, "Worked", days_worked, "this week")
            print(employee_name, "received total weekly play of", week_pay)

        elif days_worked == 5:
            for number in range(5):
                pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
                total_pay += pay
                week_pay_due = total_pay * NUMBER_DAYS

                days_worked += 7

                if pay <= 50:
                    week_pay = week_pay_due / 0.04
                    print(employee_name, "received a bonus of", week_pay)
                elif pay >= 50:
                    week_pay += week_pay
                print(employee_name, "did not receive a bonus")

            print("Basic Weekly Pay Due:", week_pay_due)
            print(employee_name, "Worked", days_worked, "this week")
            print(employee_name, "received total weekly play of", week_pay)

        elif days_worked == 6:
            for number in range(6):
                pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
                total_pay += pay
                week_pay_due = total_pay * NUMBER_DAYS

                days_worked += 7

                if pay <= 50:
                    week_pay = week_pay_due / 0.04
                    print(employee_name, "received a bonus of", week_pay)
                elif pay >= 50:
                    week_pay += week_pay
                print(employee_name, "did not receive a bonus")

            print("Basic Weekly Pay Due:", week_pay_due)
            print(employee_name, "Worked", days_worked, "this week")
            print(employee_name, "received total weekly play of", week_pay)

        else:
            for number in range(7):
                pay = int(input("Day" + str(number + 1) + "Enter hours worked:"))
                total_pay += pay
                week_pay_due = total_pay * NUMBER_DAYS

                days_worked += 7

                if pay <= 50:
                    week_pay = week_pay_due / 0.04
                    print(employee_name, "received a bonus of", week_pay)
                elif pay >= 50:
                    week_pay += week_pay
                print(employee_name, "did not receive a bonus")

            print("Basic Weekly Pay Due:", week_pay_due)
            print(employee_name, "Worked", days_worked, "this week")
            print(employee_name, "received total weekly play of", week_pay)

    if user_choice == 2:
        print("************************")
        print("*  Company Statistics  *")
        print("************************")

        week_pay_due = week_pay // week_pay_due

        print("Weekly Pay Due:")
        print("Number of staff earning bonuses:")
        print("Cost of bonuses paid")




    if user_choice == 3:
        print("************************")
        print("*   Generate Password  *")
        print("************************")
        social_number = str(input("Enter your social security number:"))
        reverse = " "
        for character in social_number:
            reverse = character + reverse
        print("Your new password is:", reverse)
    else:
        print("Exit")
