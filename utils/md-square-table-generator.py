import os
import shutil
import yaml

OUTPUT_FILE = f"..{os.sep}README.md"
IMG_PATH = f"..{os.sep}img"
IMG_PATH_FROM_README = f".{os.sep}img"
NB_COLS = 4

SQUARE_60 = 'square-1-60.png'
RECTANGLE_30 = 'rectangle-1-30.png'

def getItem(path):
    brandName = os.path.basename(path)
    basePath = path.replace(IMG_PATH, IMG_PATH_FROM_README) + os.sep
    
    item = getBrandImg(basePath + SQUARE_60, brandName)
    if os.path.exists(path + os.sep + RECTANGLE_30):
        item += f' <br /> {getBrandImg(basePath + RECTANGLE_30, brandName)}'

    yamlProps = getYamlData(path)
    if yamlProps is None:
        return f'{item} <br /> `{brandName}`'
    else:
        return f"{item} <br /> `{brandName}` <br /> {yamlProps['label']} \| [website]({yamlProps['url']})"

def getYamlData(path):
    if os.path.exists(path + os.sep + 'properties.yml'):
        with open(path + os.sep + 'properties.yml', 'r') as f:
            return yaml.safe_load(f)
    else: 
        return None

def getBrandImg(path, brandName):
    return f'![{brandName}]({winToPosixSep(path)} "{brandName}")'

def winToPosixSep(path):
    return path.replace("\\", "/")

shutil.copyfile(f".{os.sep}main-content.md", OUTPUT_FILE)

output = open(OUTPUT_FILE, "a")

# header
headerLabel = cellAlign = "|"
for i in range(0, NB_COLS):
    headerLabel += "logo|"
    cellAlign += ":--:|"

output.write(f"{headerLabel}\n")
output.write(f"{cellAlign}\n")

nbTotalItems = 0
for path, subdirs, files in os.walk(IMG_PATH):
    if path.count(os.sep) == 3: nbTotalItems += 1

colIndex = itemIndex = 0
line = ""
for path, subdirs, files in os.walk(IMG_PATH):
    # take only brand subfolders
    subdirs.sort()
    if path.count(os.sep) == 3:
        itemIndex += 1
        
        if colIndex == 0: line = "|"
        line += f"{getItem(path)}|"
        colIndex += 1

        # complete last line if needed
        if itemIndex == nbTotalItems and colIndex < NB_COLS:
            for i in range(colIndex, NB_COLS):
                line += "...|"
            output.write(line + "\n")

        if colIndex == NB_COLS:
            output.write(line + "\n")
            colIndex = 0

output.close()

