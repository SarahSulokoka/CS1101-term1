# Part (a): Employee Data Management Operations

print("PART (a): EMPLOYEE DATA MANAGEMENT")

# Task 1: Create initial list of 10 employees
employees = ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Ethan Hunt', 
             'Fiona Gallagher', 'George Miller', 'Hannah Stark', 'Ian Fleming', 'Julia Roberts']

print("1. Initial employee list:")
print(employees)
print("Total employees:", len(employees))

# Task 2: Split list into two sub-lists
subList1 = employees[:5]  # First 5 employees
subList2 = employees[5:]  # Last 5 employees

print("2. After splitting into two sub lists:")
print("subList1:", subList1)
print("subList2:", subList2)

# Task 3: Add new employee to subList2
subList2.append("Kriti Brown")
print("3. After adding new employee to subList2:")
print("subList2:", subList2)

# Task 4: Remove second employee from subList1
removed_employee = subList1.pop(1)
print("4. After removing second employee from subList1:")
print("Removed employee:", removed_employee)
print("subList1 after removal:", subList1)

# Task 5: Merge both lists
merged_list = subList1 + subList2
print("5. After merging both lists:")
print("Merged list:", merged_list)
print("Total employees in merged list:", len(merged_list))

# Task 6: Create salary list and apply 4% raise
initial_salaries = [50, 65, 45, 70, 55, 60, 80, 75, 68, 72, 58]
salaryList = [salary * 1.04 for salary in initial_salaries]

print("6. Salary operations:")
print("Initial salaries:", initial_salaries)
print("Salaries after 4% raise:", [round(salary, 2) for salary in salaryList])

# Task 7: Sort salaries and show top 3
sorted_salaries = sorted(salaryList, reverse=True)
top_3_salaries = sorted_salaries[:3]

print("7. Top 3 salaries after raise:")
for i, salary in enumerate(top_3_salaries, 1):
    print(f"{i}. ${salary:.2f}K")