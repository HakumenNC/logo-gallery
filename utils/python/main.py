import os
import shutil

from fileutils import FileUtils, OUTPUT_FILE, OUTPUT_SETS_FILE, RELATIVE_IMG_PATH, RELATIVE_SET_PATH
from markdownutils import MarkdownUtils, NB_COLS, SQUARE_60, SQUARE_B_60, RECTANGLE_30, RECTANGLE_B_40

shutil.copyfile(f"..{os.sep}main-content.md", OUTPUT_FILE)
output = open(OUTPUT_FILE, "a")
output_sets = open(OUTPUT_SETS_FILE, "w")

nbItems = FileUtils.count_brand_items()

logos = []
### sets
output_sets.write("# Sets")
output_sets.write("\n")
output_sets.write(f"|set|logos|\n|:--:|:---|\n")
for path, subdirs, files in os.walk(RELATIVE_SET_PATH):
    if path.count(os.sep) == 3 and 'brands' not in path and 'other' not in path:
        props = FileUtils.get_properties_item(path)
        row = f"|{MarkdownUtils._get_img(path, SQUARE_60)}<br />`{os.path.basename(path)}`|"
        if props is not None:
            logos.extend(props['logos'])
            for item in sorted(props['logos']):
                row += f"{MarkdownUtils._get_img_by_code(item, RECTANGLE_B_40, RECTANGLE_30)} "
        else: 
            row += "..."
        row += "|\n"
        output_sets.write(row)

other_path = RELATIVE_SET_PATH + os.sep + 'other'
props = FileUtils.get_properties_item(other_path)
row = f"|{MarkdownUtils._get_img(other_path, SQUARE_60)}<br />`{os.path.basename(other_path)}`|"
for path, subdirs, files in os.walk(RELATIVE_IMG_PATH):
    if FileUtils.is_brand_folder(path) and os.path.basename(path) not in logos:
        row += f"{MarkdownUtils._get_img_by_code(os.path.basename(path), RECTANGLE_B_40, RECTANGLE_30)} "

row += "|\n"
output_sets.write(row)

output_sets.write("\n")
output_sets.close()

### full gallery

# header
output.write(MarkdownUtils.build_gallery_headers())

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

