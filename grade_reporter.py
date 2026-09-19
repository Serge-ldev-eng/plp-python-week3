scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    total = total + score
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    print(f"{score} - {grade}")
    
    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(scores)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")