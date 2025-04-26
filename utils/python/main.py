import os
import shutil

from fileutils import FileUtils, OUTPUT_FILE, RELATIVE_IMG_PATH
from markdownutils import MarkdownUtils, NB_COLS

shutil.copyfile(f"..{os.sep}main-content.md", OUTPUT_FILE)
output = open(OUTPUT_FILE, "a")
nbItems = FileUtils.count_brand_items()

# header
output.write(MarkdownUtils.build_headers())

# rows
colIndex = itemIndex = 0
row = ""
for path, subdirs, files in os.walk(RELATIVE_IMG_PATH):
    if FileUtils.is_brand_folder(path):
        itemIndex += 1
        
        if colIndex == 0: row = "|"

        row += f"{MarkdownUtils.build_brand_item(path)}|"
        colIndex += 1

        # complete last line if needed
        if itemIndex == nbItems and colIndex < NB_COLS:
            for i in range(colIndex, NB_COLS): row += "...|"
            output.write(row + "\n")

        if colIndex == NB_COLS:
            output.write(row + "\n")
            colIndex = 0

output.close()

