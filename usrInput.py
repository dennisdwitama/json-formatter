import os.path


def checkPath(filePath, dataFiles):
    if not os.path.exists(filePath):
        print(filePath + " does not exist.")
        return "doesn't exist"
    
    elif os.path.isdir(filePath):
        for file in os.listdir(filePath):
            checkPath(os.path.join(filePath, file), dataFiles)
            dataFiles.append(filePath)

    else:
        if filePath.endswith("_formatted.json"):
            pass
        elif filePath.endswith(".json"):
            dataFiles.append(filePath)

    return tuple(dataFiles)
