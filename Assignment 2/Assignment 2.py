import matplotlib.pyplot as plt

with open('student_data.csv', 'r') as file:
    lines = file.readlines()

# Remove the header
data = lines[1:]

genders = []
results = []

for line in data:
    name, gender, math_marks, english_marks = line.strip().split(',')
    
    genders.append(gender)
    
    if int(math_marks) < 40 or int(english_marks) < 40:
        results.append('Fail')
    else:
        results.append('Pass')

gender_counts = { 'Male': genders.count('Male'), 'Female': genders.count('Female') }

result_counts = { 'Pass': results.count('Pass'), 'Fail': results.count('Fail') }

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].pie(gender_counts.values(), labels=gender_counts.keys(), autopct='%1.1f%%')
axs[0].set_title('Gender Distribution')

axs[1].pie(result_counts.values(), labels=result_counts.keys(), autopct='%1.1f%%')
axs[1].set_title('Pass/Fail Distribution')

plt.tight_layout()
plt.show()