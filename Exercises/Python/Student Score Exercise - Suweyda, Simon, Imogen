# General comments
# Charles has good knowledge of programming principles and did well in this module.
# He contributed to group discussion/questions and worked well in groups.
import os
understanding = ''
contribution = ''
punctuation = ''
engagement = ''

# Mapping levels to descriptive words
level_data = {
    1: 'poor',
    2: 'below average',
    3: 'decent',
    4: 'good',
    5: 'excellent'
}

# Function to gather user data
def get_user_data():
    user_data = {}
    print("Note: This loop should be changed to 16 but it's 2 so you can test without inputting all names/scores at once!\n")
    for i in range(2):  # Modify the range as required for more students
        name = input("Enter your student's name:\n")
        understanding_level = int(input(f"What was {name}'s understanding level in this module from 1-5:\n"))
        contribution_level = int(input(f"What was {name}'s contribution level in this module from 1-5:\n"))
        punctuation_level = int(input(f"What was {name}'s punctuation level in this module from 1-5:\n"))
        engagement_level = int(input(f"What was {name}'s engagement level in this module from 1-5:\n"))
        user_data[name] = {
            "understanding_level": level_data.get(understanding_level, 'unknown'),
            "contribution_level": level_data.get(contribution_level, 'unknown'),
            "punctuation_level": level_data.get(punctuation_level, 'unknown'),
            "engagement_level": level_data.get(engagement_level, 'unknown'),
        }
    return user_data
16
# Calling the function to test
students_data = get_user_data()

# Ensure the directory for storing files exists

if not os.path.exists("students"):
    os.makedirs("students")

# Function to save a report for a student
def save_out_file(text, name):
    file_path = os.path.join("students", f"{name}.txt")
    with open(file_path, "w") as file:
        file.write(text)
    # Optional: Open file in Notepad for review
    os.system(f"notepad.exe {file_path}")

# Example: Saving reports for each student in user_data
for name, data in students_data.items():
    template = (
        f"General comments:\n{name} did {data['understanding_level']} in this module in terms of understanding.\n"
        f"{name}'s contribution level was {data['contribution_level']}.\n"
        "Recommendations:\nContinue to practice and explore good code design and start to specialize in areas of interest.\n"
      f"{name}'s punctuation level was {data['punctuation_level']} and their engagement level was {data['engagement_level']} throughout the module with camera on.\n"

    )
    save_out_file(template, name)


# well done guys -suweyda
# yeah well done!! - zeki
