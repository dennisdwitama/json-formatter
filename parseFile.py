import json
import os

def getJSONContent(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("JSON content must be a list of employee dictionaries.")
    
    return data

def generateEmail(firstName, lastName):
    email = f"{firstName[0].lower()}{lastName.lower()}@comp.com"
    return email

def generateFormattedFile(empList, ogPath):
    base_path, _ext = os.path.splitext(ogPath)

    # Create formatted file output
    output_path = base_path + "_formatted.json"

    # Write employee entries to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(empList, f, indent=4)

def generateSalary(jobID, state):
    if jobID.startswith("SA_"):
        base = 60000
    elif jobID.startswith("IT_"):
        base = 80000
    elif jobID.startswith("HR_"):
        base = 70000
    else:
        base = 0

    is_manager = jobID.endswith("_MGR")
    if is_manager:
        mgr_bonus = 0.05 * base
    else:
        mgr_bonus = 0

    state_bonus = 0.015 * base if state in ["NY", "CA", "WA", "OR", "VT"] else 0

    return base + mgr_bonus + state_bonus

def processEachEmp(empList):
    processed = []
    for emp in empList:
        valid_phone = validatePhoneNumber(emp.get("Phone Number", ""))
        valid_zip = validateZips(emp.get("Zip Code", ""))
        if valid_phone == 1 or valid_zip == 1:
            print
            continue

        if emp:
            emp.pop("I declare that the above information is accurate.", None)
        
        firstName = emp.get("First Name", "")
        lastName = emp.get("Last Name", "")
        emp["Email"] = generateEmail(firstName, lastName)

        jobID = emp.get("Job ID", "")
        state = emp.get("State", "")
        emp["Salary"] = generateSalary(jobID, state)

        emp["Phone Number"] = valid_phone
        emp["Zip Code"] = valid_zip

        processed.append(emp)

    return processed


def validatePhoneNumber(phone):
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return int(digits)
    else:
        return 1
    
def validateZips(zipCode):
    digits = ''.join(filter(str.isdigit, zipCode))
    if len(digits) == 5:
        return int(digits)
    else:
        return 1