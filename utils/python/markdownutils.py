import os
import yaml

from fileutils import FileUtils, ABSOLUTE_IMG_PATH, RELATIVE_IMG_PATH

NB_COLS = 3
SQUARE_60 = 'square-1-60.png'
RECTANGLE_30 = 'rectangle-1-30.png'
SQUARE_B_60 = 'square-b-1-60.png'
RECTANGLE_B_40 = 'rectangle-b-1-40.png'

class MarkdownUtils:

    @staticmethod
    def build_gallery_headers():
        headerLabel = cellAlign = "|"
        
        for i in range(0, NB_COLS):
            headerLabel += "logo|"
            cellAlign += ":--:|"
        
        return f"{headerLabel}\n{cellAlign}\n"
    
    @staticmethod
    def build_brand_item(path):
        result = ""
        result += MarkdownUtils._get_img_by_code(os.path.basename(path), SQUARE_B_60, SQUARE_60)
        result += f' <br />{MarkdownUtils._get_img_by_code(os.path.basename(path), RECTANGLE_B_40, RECTANGLE_30)}'

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
    
    @staticmethod
    def _get_img_by_code(code, format):
        p = ABSOLUTE_IMG_PATH + os.sep + code[0] + os.sep + code + os.sep + format
        return f'![{code}]({FileUtils.convert_path_to_posix(p)} "{code}")'
    
    @staticmethod
    def _get_img_by_code(code, format, formatIfNull=None):
        basePath = RELATIVE_IMG_PATH + os.sep + code[0] + os.sep + code + os.sep
        exist = os.path.exists(basePath + os.sep + format)
        path = ''
        if exist:
            path = ABSOLUTE_IMG_PATH + os.sep + code[0] + os.sep + code + os.sep + format
        else:
            path = ABSOLUTE_IMG_PATH + os.sep + code[0] + os.sep + code + os.sep + formatIfNull

        return f'![{code}]({FileUtils.convert_path_to_posix(path)} "{code}")'
