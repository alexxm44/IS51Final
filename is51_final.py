"""
The program is trying to display the number of grades, the average grade, and the percentage of grades shown from the list in txt file
divide the total by the sum of the grades that are provided in that file
find out how many values are above the average grade. divide that number by the how many values there are.
configure a percentage and then round it
"""

"""
main():
    open the txt as an infile
    allocte the lines of the list
    close the code file
    calculate_percent_above_average()
calculate_percent_above_average():
number of lines = len()
total = total()
average = total/number of lines
iterate through the lines:
if it is above the average: 
    number of values = number of values + 1

percent above average = above average + number of values
"""

def main():
    calculate_percent_above_average(grades())

def grades():
    infile = open('Final.txt', 'r')
    lines = infile.readlines()
    grades = [int(i) for i in lines]
    return grades

def calculate_percent_above_average(grades):
    sum = 0
    for i in grades:
        average = sum / len(grades)

    num_above_average = 0
    for i in grades:
        if i > average:
            num_above_average = num_above_average + 1

    percent_above = round((num_above_average / average) * 100, 2)
    print("{percent_above}% of values that are higher than average")

main()