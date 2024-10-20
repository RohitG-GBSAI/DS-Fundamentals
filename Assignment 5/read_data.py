def read_file(path):
    data = []
    with open(path) as file:
        for row in file.readlines():
            data.append(row.strip("\n").split(","))
    return data

if __name__ == "__main__":
    print(read_file("caloriedata.csv"))
