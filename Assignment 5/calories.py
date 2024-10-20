from read_data import read_file

class Calories:
    def __init__(self, start, end, path) -> None:
        self.data = read_file(path)
        self.start = self.calculate_date(start)
        self.end = self.calculate_date(end)

    def avg(self):
        total_calories = sum([int(cal) for cal in self.get_data()])
        return total_calories / len(self.get_data()) if self.get_data() else 0

    def std(self):
        avg_val = self.avg()
        variance = sum([(float(cal) - avg_val) ** 2 for cal in self.get_data()]) / len(self.get_data())
        return variance ** 0.5

    def highest_cal(self):
        daily_totals = []
        current_total = 0
        previous_date = self.start
        
        for date, cal in self.data:
            date_numeric = self.calculate_date(date)
            if self.start <= date_numeric <= self.end:
                if date_numeric == previous_date:
                    current_total += int(cal)
                else:
                    daily_totals.append(current_total)
                    current_total = int(cal)
                    previous_date = date_numeric
            elif date_numeric > self.end:
                break
        daily_totals.append(current_total)
        return max(daily_totals)

    def highest_meal_cal(self):
        return max([int(cal) for cal in self.get_data()])

    def get_data(self):
        filtered_data = [cal for date, cal in self.data if self.start <= self.calculate_date(date) <= self.end]
        return filtered_data

    @staticmethod
    def calculate_date(date):
        day, month, year = map(int, date.split("/"))
        return year * 10000 + month * 100 + day  # Simple numerical comparison

