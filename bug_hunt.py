count = 1
total = 0

# BUG: Missing colon at end of while line, Python needs : to start the loop block
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Condition was count < 5 which only adds 1 to 4 (10), should be <=5 to include 5 and get 15
# BUG: Cannot add string and integer with +, need to convert total to string with str() or use f-string
print("Sum of 1 to 5 is: " + str(total))