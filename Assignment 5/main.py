from calories import Calories

if __name__ == "__main__":
    # Date format should be DD/MM/YYYY
    c = Calories("02/07/2024", "30/08/2024", "caloriedata.csv")

    print("Average Calories Per Day:", c.avg())
    print("Standard Deviation:", c.std())
    print("Highest Calories in a Day:", c.highest_cal())
    print("Highest Calories in a Meal:", c.highest_meal_cal())
