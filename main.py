import usrInput
import sys
import json
import parseFile
import os


def main():
    checkReturn = usrInput.checkPath(r'sprint_project/testFiles/01threeDict.json', [])
    errorHandle(checkReturn)
    startProcess(checkReturn)

def errorHandle(checkReturn):
    if checkReturn == 1:
        sys.exit(1)

    if not isinstance(checkReturn, tuple):
        sys.exit(1)

    if len(checkReturn) == 0:
        sys.exit(0)

def printOutput(numFiles, numEmps):
    print("============================================================")
    print("---------------------Processing Summary---------------------")
    print("============================================================")
    print(f" Number of files processed:   {numFiles}")
    print("Number of employee entries")
    print(f"  formatted and calculated:   {numEmps}")

def startProcess(tup):
    numFiles = 0
    numEmps = 0
    for filePath in tup:
        if isinstance(filePath, str) and filePath.lower().endswith(".json"):
            emp = parseFile.getJSONContent(filePath)
            emp_formatted = parseFile.processEachEmp(emp)
            parseFile.generateFormattedFile(emp_formatted, filePath)

            numFiles += 1
            numEmps += len(emp)

    printOutput(numFiles, numEmps)

if __name__ == "__main__":
    main()