def calc_mileage(weeks, mileage_goal, growth_rate):
    upcoming_weeks = [0]
    i=0
    while upcoming_weeks[i] < mileage_goal:
        four_week_average = int(sum(weeks) / len(weeks))
        next_week = int(four_week_average * growth_rate)
        weeks.remove(weeks[0])
        weeks.append(next_week)
        upcoming_weeks.append(next_week)
        i+=1

    return upcoming_weeks[1:len(upcoming_weeks)]




def main():
    print()
    print("Enter your mileage for the last 4 weeks of training and the\nprogram will return your ideal "
          "mileage buildup. Each weeks \nmileage is increased by a % of the previous 4-week total.")
    print()
    print("NOTE: This program does not take into account injury, down weeks, etc... \nThis is simply a loose guideline of your mileage increase.")
    print()
    print("Extended Note: If soad consumed within 4 week period,\nscrap the training completely and start at 0")
    print()
    week1 = int(input("Enter mileage for week 1:"))
    week2 = int(input("Enter mileage for week 2:"))
    week3 = int(input("Enter mileage for week 3:"))
    week4 = int(input("Enter mileage for week 4:"))

    goal_mileage = int(input("What is your goal mileage?: "))
    growth_rate = float(input("What rate would you like to grow. Ex: 1.1, 1.15, 1.25 etc...:"))

    weeks = [week1, week2, week3, week4]

    print()
    print("Mileage entered")
    print()
    for i in range(len(weeks)):
        print("Week", i+1, "Mileage:", weeks[i])
    result_array = calc_mileage(weeks,goal_mileage, growth_rate)

    print()
    print("Future Mileage")
    print()
    for i in range(len(result_array)):

        print("Week", i + 5, "Mileage:", result_array[i]) # add 5 as there are 4 weeks before it, plus 1 as i starts at 0
    print()
    print("It took you",len(result_array),"weeks to reach your goal mileage of", goal_mileage)

    print()
    print("Editors note: Don't follow this\ncalculation and run 120mpw instead :)")

main()
