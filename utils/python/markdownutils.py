import os
import yaml

from fileutils import FileUtils

NB_COLS = 3
SQUARE_60 = 'square-1-60.png'
RECTANGLE_30 = 'rectangle-1-30.png'

class MarkdownUtils:

    @staticmethod
    def build_headers():
        headerLabel = cellAlign = "|"
        
        for i in range(0, NB_COLS):
            headerLabel += "logo|"
            cellAlign += ":--:|"
        
        return f"{headerLabel}\n{cellAlign}\n"
    
    @staticmethod
    def build_brand_item(path):
        result = MarkdownUtils._get_img(path, SQUARE_60)
        if os.path.exists(path + os.sep + RECTANGLE_30):
            result += f' <br /> {MarkdownUtils._get_img(path, RECTANGLE_30)}'

        result += f' <br /> `{os.path.basename(path)}`'

        props = FileUtils.get_properties_item(path)
        if props is None:
            return result
        else:
            return f"{result} <br /> {props['label']} \| [website]({props['url']})"
    
    @staticmethod
    def _get_img(path, format, toAbsolute=True):
        if toAbsolute == False:
            p = path + os.sep + format
        else:
            p = FileUtils.to_absolute_path(path + os.sep + format)
        return f'![{os.path.basename(path)}]({FileUtils.convert_path_to_posix(p)} "{os.path.basename(path)}")'
