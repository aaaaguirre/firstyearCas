from statistics import mean
food_list = [["Monday", 74, 1500, 6000],
             ["Tuesday", 60, 2500, 4000],
             ["Wednesday", 80, 3000, 3000],
             ["Thursday", 30, 2900, 7000]]
print('*' * 50)
print("\t       Food Tracking System         ")
print('*' * 50)
print("\t 1) Add a Day        ")
print("\t 2) Under 2000 Calories       ")
print("\t 3) Salt Intake per Calorie")
print("\t 4) Highest Day   ")
print("\t 5) Exit             ")
print('*' * 50)
menu_option = int(input("\tPlease enter option:"))

# main menu loop
while menu_option != 5:
    if menu_option == 1:
        print('*' * 50)
        print("\t\t{:^100}".format("Day's Details"))
        print('*' * 100)
        print("\t\t{:10}".format("Day") +
              "{:25}".format("No. of minutes of exercise") +
              "{:30}".format("No. of calories consumed") +
              "{:50}".format("No. of msg of salt consumed "))
        print('*' * 100)
        for food in food_list:
            print("\t\t{:12}".format(food[0]) +
                  "{:25}".format(food[1]) +
                  "{:30}".format(food[2]) +
                  "{:30}".format(food[3]))
        print("\n")
    elif menu_option == 2:
        print('*' * 50)
        print("\t\t{:^25}".format("Days under 2000 calories"))
        print('*' * 50)
        count_low = 0
        print("\t\t{:12}".format("Day") +
              "{:10}".format("Calories Taken"))
        print('*' * 50)
        for row in food_list:
            if row[2] <= 2000:
                count_low += 1
                print("\t\t{:12}".format(row[0]) +
                      "{:10}".format(row[2]))
        print('*' * 50)
        print()
    elif menu_option == 3:
        print('*' * 100)
        print("\t\t{:^80}".format("Average salt intake per calorie"))
        print('*' * 100)
        print("\t\t", end='')
        print("\t\t{:12}".format("Day") +
              "{:20}".format("Calories taken") +
              "{:15}".format("Salt taken") +
              "{:15}".format("Average salt intake (mh) per calorie"))
        print('*' * 100)
        for row in food_list:
            average_salt = mean([row[3] for row in food_list])
            per_calorie = (row[3] / row[2])
            per_calorie = round(per_calorie, 2)
            print("\t\t{:12}".format(row[0]) +
                  "{:25}".format(row[2]) +
                  "{:30}".format(row[3]) +
                  "{:30}".format(per_calorie))
    elif menu_option == 4:
        count_high = 0
        print("Highest Day : \t\tCalories intake:")
        for row in food_list:
            if row[2] == 3000:
                count_high += 1
                print("\t\t{:12}".format(row[0]) +
                      "{:10}".format(row[2]))
    else:
        print("Invalid Option")
    print('*' * 50)
    print("\t       Food Tracking System         ")
    print('*' * 50)
    print("\t 1) Add a Day        ")
    print("\t 2) Under 200 Calories       ")
    print("\t 3) Salt Intake per Calorie")
    print("\t 4) Highest Day   ")
    print("\t 5) Exit             ")
    print('*' * 50)
    menu_option = int(input("\tPlease enter option:"))
