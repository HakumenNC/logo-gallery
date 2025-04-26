import os
import yaml

OUTPUT_FILE = f"..{os.sep}..{os.sep}README.md"
RELATIVE_IMG_PATH = f"..{os.sep}..{os.sep}img"
ABSOLUTE_IMG_PATH = f".{os.sep}img"
PROPERTIES_ITEM_FILE = 'properties.yml'

class FileUtils:

    @staticmethod
    def count_brand_items():
        nbItems = 0
        for path, subdirs, files in os.walk(RELATIVE_IMG_PATH):
            if FileUtils.is_brand_folder(path): nbItems += 1
        return nbItems

    @staticmethod
    def is_brand_folder(path):
        return path.count(os.sep) == 4
    
    @staticmethod
    def convert_path_to_posix(path):
        return path.replace("\\", "/")
    
    @staticmethod
    def to_absolute_path(path):
        return path.replace(RELATIVE_IMG_PATH, ABSOLUTE_IMG_PATH)
    
    @staticmethod
    def get_properties_item(path):
        p = path + os.sep + PROPERTIES_ITEM_FILE
        if os.path.exists(p):
            with open(p, 'r') as f:
                return yaml.safe_load(f)
        else:
            return None  