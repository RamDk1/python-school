# Ramses Rodriguez Barroso

# List of universities
universities = [
    ["Park University Gilbert", [
        ["Computer Science",["Data Structures", "Algorithms", "Machine Learning"]],
        ["Physics",["Quantum Mechanics", "Electromagnetism", "Thermodynamics"]]
    ]],
    ["Park University Missouri", [
        ["Mathematics",["Calculus I","Linear Algebra","Discrete Math"]],
        ["Literature",["Shakespeare","Modern Poetry","Creative Writing"]]
    ]],
]

# Print the data
print("Universities and courses:")
for university in universities:
    universituy_name, departments = university
    print(f"\n{universituy_name}:")
    for department in departments:
        department_name, courses = department
        print(f"  Department: {department_name}")
        print(f"    Courses: {', ' .join(courses)}")
