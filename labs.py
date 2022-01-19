# Solutions for exercise 3. Python Tutorial
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


print("The Miles Per Gallon program\n")

miles_driven = float(input("Enter miles driven: \n"))
gallons = float(input("Enter gallons of gas used: \n"))

result = miles_driven/gallons

print("\nMiles Per Gallon: ", round(result,2))
print("\nBye")

print("The Test Score Program\n")

print("Enter 3 test scores \n" +
     "==================== ")
# ------- solution 1 --------------
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))

total = score1 + score2 + score3
average = total/3
# -------- solution 2 -------------
counter = 0
sum = 0
while counter < 3:
    score = int(input("\nEnter your score: "))
    sum += score
    counter += 1

total = sum
average = float(total/3)

# Display output to user
print("==================== \n")
print("Total score: ", total)
print("Average score: ", round(average, 2))

