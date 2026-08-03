def department_summary(employees):

    if employees == []:                         # Return empty dictionary if no employees
        return {}

    details = {}                                # Stores department wise details

    for employee in employees:

        department = employee["department"]

        if department not in details:           # If department is new, create it
            details[department] = {
                "count": 0,
                "total": 0,
                "highest": employee["salary"],
                "top": employee["name"]
            }

        details[department]["count"] += 1
        details[department]["total"] += employee["salary"]

        if employee["salary"] > details[department]["highest"]:
            details[department]["highest"] = employee["salary"]
            details[department]["top"] = employee["name"]

    output = {}

    for department in sorted(details):          # Departments in alphabetical order

        count = details[department]["count"]
        average = round(details[department]["total"] / count, 2)
        top_name = details[department]["top"]

        output[department] = (count, average, top_name)

    return output


employees = [
    {"name": "Tisha", "department": "Engineering", "salary": 76500},
    {"name": "Arnold", "department": "IT", "salary": 43800},
    {"name": "Khushi", "department": "HR", "salary": 52700},
    {"name": "Anas", "department": "Sales", "salary": 59200},
    {"name": "Karan", "department": "Engineering", "salary": 84600},
    {"name": "Aman", "department": "Sales", "salary": 61500},
    {"name": "Saad", "department": "Engineering", "salary": 71800},
    {"name": "Harsh", "department": "IT", "salary": 50100}
]

print(department_summary(employees))
