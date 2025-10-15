# Part (a): Employee Data Management Operations

print("PART (a): EMPLOYEE DATA MANAGEMENT")

# Initial list of 10 employees
employees = ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Ethan Hunt', 
             'Fiona Gallagher', 'George Miller', 'Hannah Stark', 'Ian Fleming', 'Julia Roberts']

print("1. Initial employee list:")
print(employees)
print("Total employees:", len(employees))

# List Slicing: list[:5] gets first 5 elements, list[5:] gets remaining elements
subList1 = employees[:5]  # First 5 employees
subList2 = employees[5:]  # Last 5 employees

print("2. After splitting into two sub lists:")
print("subList1:", subList1)
print("subList2:", subList2)

# List Methods: append() adds to end of list
subList2.append("Kriti Brown")
print("3. After adding new employee to subList2:")
print("subList2:", subList2)

# List Methods: pop() removes by index and returns the removed element
removed_employee = subList1.pop(1)
print("4. After removing second employee from subList1:")
print("Removed employee:", removed_employee)
print("subList1 after removal:", subList1)

# List Concatenation: + operator merges lists
merged_list = subList1 + subList2
print("5. After merging both lists:")
print("Merged list:", merged_list)
print("Total employees in merged list:", len(merged_list))

# Create salary list
initial_salaries = [50, 65, 45, 70, 55, 60, 80, 75, 68, 72, 58]

# List Comprehension: Efficient way to apply operations to list elements
salaryList = [salary * 1.04 for salary in initial_salaries]

print("6. Salary operations:")
print("Initial salaries:", initial_salaries)
print("Salaries after 4% raise:", [round(salary, 2) for salary in salaryList])

# Sorting: sorted() with reverse=True gives descending order
sorted_salaries = sorted(salaryList, reverse=True)
top_3_salaries = sorted_salaries[:3]

print("7. Top 3 salaries after raise:")
for i, salary in enumerate(top_3_salaries, 1):
    print(f"{i}. ${salary:.2f}K")