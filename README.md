# Employee Information Processing Script

This repository contains the script for processing employee data from raw input files (JSON or PDF) and generating a formatted JSON file for easy entry into a database. The script is designed to automate the process of converting employee data from raw formats into a clean and formatted output that DB administrators can use.

## Objective
The main purpose of the script is to take raw employee information, either as a JSON or PDF file, and generate a formatted JSON file for Database (DB) Admins so they can easily enter new employees into the DB. The project is internally developed to fix and enhance existing functionality, making the process more efficient.

## Existing Code

### `main.py`
#### `main()`
- **Arguments**: None
- **Returns**: None
- **Functionality**: Initiates the script by invoking the required functions to process the employee information.

### `usrInput.py`
#### `checkPath(filePath, dataFiles)`
- **Arguments**: 
  - `filePath` (str) – The file path to the JSON, PDF, or folder.
  - `dataFiles` (list) – A list to store the valid file paths.
- **Returns**: 
  - `int` - `1` if the path does not exist (error code).
  - `tuple` - Tuple of valid file paths.
- **Functionality**: Checks if the given file path exists and if the file is a valid JSON or PDF for processing. Skips already formatted JSON files.

## New Code

### `main.py`
#### `errorHandle(checkReturn)`
- **Arguments**: 
  - `checkReturn` (int or tuple) – Return value from the `checkPath` function.
- **Returns**: None
- **Functionality**: Exits the script if the path is invalid or if no valid files are available for processing.

#### `printOutput(numFiles, numEmps)`
- **Arguments**: 
  - `numFiles` (int) – The number of valid files processed.
  - `numEmps` (int) – The number of employee entries processed.
- **Returns**: None
- **Functionality**: Displays a summary of the number of files and employees processed.

#### `startProcess(tup)`
- **Arguments**: 
  - `tup` (tuple) – Tuple of valid JSON or PDF file paths.
- **Returns**: None
- **Functionality**: Processes each valid file and saves the formatted employee data to a new JSON file.

### `parseFile.py`
#### `getJSONContent(file)`
- **Arguments**: 
  - `file` (str) – The path to the JSON file.
- **Returns**: 
  - `list` – A list of dictionaries containing employee data.
- **Functionality**: Reads and extracts the content of the JSON file.

#### `generateEmail(firstname, lastname)`
- **Arguments**: 
  - `firstname` (str) – The employee's first name.
  - `lastname` (str) – The employee's last name.
- **Returns**: 
  - `str` – The generated email in the format `<first initial><last name>@company.com`.
- **Functionality**: Generates a standardized company email for the employee.

#### `generateFormattedFile(empList, ogPath)`
- **Arguments**:
  - `empList` (list) – List of employee entries to be saved.
  - `ogPath` (str) – The original file path.
- **Returns**: None
- **Functionality**: Saves the formatted employee data to a new JSON file with a "_formatted" suffix.

#### `generateSalary(jobId, state)`
- **Arguments**:
  - `jobId` (str) – Employee job ID (e.g., `IT_REP`, `HR_MNG`).
  - `state` (str) – Employee's US state.
- **Returns**: 
  - `float` – The calculated salary based on job ID and state.
- **Functionality**: Calculates the salary based on base salary, manager status, and location bonuses.

#### `processEachEmp(empList)`
- **Arguments**:
  - `empList` (list) – List of employee entries.
- **Returns**: 
  - `list` – A list of formatted employee entries.
- **Functionality**: Processes and formats employee data (validates phone numbers, zip codes, capitalizes names, generates email, and salary).

#### `validatePhoneNumber(phoneNumber)`
- **Arguments**:
  - `phoneNumber` (str) – Employee phone number.
- **Returns**:
  - `int` – Valid 10-digit phone number or error code.
- **Functionality**: Validates if the phone number is a valid 10-digit number.

#### `validateZips(zipCode)`
- **Arguments**:
  - `zipCode` (str) – Employee zip code.
- **Returns**:
  - `int` – Valid 5-digit zip code or error code.
- **Functionality**: Validates if the zip code is a valid 5-digit number.

### `usrInput.py`
#### `getUsrInput(msg)`
- **Arguments**: 
  - `msg` (str) – Message to prompt the user for input.
- **Returns**: 
  - `str` – The input from the user.
- **Functionality**: Prompts the user for input and returns their response.

## Installation
To install and run the script, follow these steps:

1. Clone this repository.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt