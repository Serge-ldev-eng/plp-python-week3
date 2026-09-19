count = 1
total = 0

# BUG: Missing colon at end of while statement. Added : to make it valid syntax.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Logic bug - condition was count < 5 so it only summed 1 to 4 (10). Changed to count <= 5 to include 5 and get 15. This had no error message, only wrong result.
# BUG: Cannot concatenate string and integer with +. Fixed by converting total to string with str().

print("Sum of 1 to 5 is: " + str(total))