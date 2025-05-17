import os
import shutil

from fileutils import FileUtils, OUTPUT_FILE, RELATIVE_IMG_PATH
from markdownutils import MarkdownUtils, NB_COLS, RECTANGLE_30, SQUARE_60

output = open(f"./export/wall.md", "w")

# rows

for path, subdirs, files in os.walk(RELATIVE_IMG_PATH):
    if FileUtils.is_brand_folder(path):
         output.write(MarkdownUtils._get_img('../' + path, RECTANGLE_30, False))

output.close()

