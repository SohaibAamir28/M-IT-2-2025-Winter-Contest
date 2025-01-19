import sys
input = sys.stdin.read

def calculate_trimmed_mean(N, grades):
    # Sort the grades to remove the N highest and N lowest
    grades.sort()
    # Ensure there are enough grades to remove
    if len(grades) < 5 * N:
        raise ValueError("The number of grades does not match the expected 5 * N.")
    # Remove the N lowest and N highest grades
    trimmed_grades = grades[N:-N]
    # Calculate the average of the remaining grades
    return sum(trimmed_grades) / len(trimmed_grades)

# Input
lines = input().splitlines()
N = int(lines[0])
grades = list(map(int, lines[1].split()))

# Validate input
if len(grades) != 5 * N:
    raise ValueError("The number of grades must be exactly 5 * N.")

# Calculate and print the trimmed mean
result = calculate_trimmed_mean(N, grades)
print(f"{result:.15f}")
