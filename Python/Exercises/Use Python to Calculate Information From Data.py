data=[90,30,13,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]

# There are three parts to this task:

# Part 1 - Using a list, you will be required to calculate and print to the console the following information:
# The number of students' marks in the data sample.
print("\nPart 1:\n")
numberMarks = len(data) # len() calculates the length of the list and I've stored it as a variable for later
print(f"There are {numberMarks} different students' marks.")

# The lowest and highest marks.
lowestMark = min(data) # min() calculates the lowest value in the list
print(f"The lowest mark was {lowestMark}.")

highestMark = max(data) # max() calculates the highest value in the list
print(f"The highest mark was {highestMark}.")

# The average mark, formatted to two decimal places.
totalMarks = sum(data) # sum() calculates the total of the list
averageMarks = ("%.2f" %(totalMarks / numberMarks)) # calculating the average using total / length, and formatting it as 2dp
print(f"The total marks were {totalMarks} and the average was {averageMarks}.")


# Part 2 - you will be required to write code to process the data and calculate how many instances of marks in the categories shown below. Alongside each category you should print out one asterisk for each occurrence. As an example, the category 10-20 has four occurrences (13, 17, 16, & 14) and therefore has four asterisks, e.g.:
# Mark Count   0 - 10 0   10 - 20 4 **** 20 - 30 7 ******* 30 - 40 8 ******** 40-50 11 *********** 50 - 60 9 ********* 60 -70 8 ********
print("\nPart 2:\n")
ranges = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80), (80, 90), (90, 100)] # Creates a list with all the ranges

rangeCounts = {f"{start}-{end}": 0 for start, end in ranges} # Creates a dictionary containing the ranges starting off with a value of 0 - to be used in the for loop

# Count the occurrences of marks in each range
for mark in data: # For loop, for every mark (value) in the list
    for start, end in ranges: # Nested for loop, for every range (value) in the ranges list
        if start <= mark < end: # Adds 1 to the quantity of ranges if the mark is within the range
            rangeCounts[f"{start}-{end}"] += 1
            break

# Print the results
for range, asteriskCount in rangeCounts.items():
    print(f"{range}: {asteriskCount} {'*' * asteriskCount}")


# Part 3 - Finally, you will be requested to calculate and print out what the pass mark should be to ensure that at least 60% of students will pass the exam. This should be to the nearest ten.
print("\nPart 3:\n")
sortedData = sorted(data) # sorted() sorts the data from lowest to highest to set up finding the index for 60%

sixtyIndex = int(0.6 * numberMarks) # Calculates 60% of the total marks and stores it as an integer to be used as the index

passMark = round(sortedData[sixtyIndex] / 10) * 10 # Grabs the mark that's in the index of the 60% mark and then rounds it to the nearest ten
print(f"The pass mark to ensure at least 60% of students pass is {passMark}.")
