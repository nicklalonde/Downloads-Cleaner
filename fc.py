import os
import collections
from pprint import pprint 

# Common File Types

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'm4v', 'h264']
EXT_IMGS = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
EXT_DOCS = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'xlsm', 'ods', 'doc', 'docx', 'hmtl', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['exe', 'dmg', 'iso']

# Create Directories

BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documeents', 'Applications', 'Other']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map Files

DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)
for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# Move to Target Directory
for f_ext, f_list in files_mapping.items():
 
    if f_ext in EXT_INSTL:
        for file in f_list:
            destination = os.path.join(BASE_PATH, 'Applications', file)
            if os.path.exists(destination):
                destination = os.path.join(BASE_PATH, 'Applications', f"{file.split('.')[0]}_1.{f_ext}")
            os.rename(os.path.join(DOWNLOADS_PATH, file), destination)
    elif f_ext in EXT_AUDIO:
        for file in f_list:
            destination = os.path.join(BASE_PATH, 'Music', file)
            if os.path.exists(destination):
                destination = os.path.join(BASE_PATH, 'Music', f"{file.split('.')[0]}_1.{f_ext}")
            os.rename(os.path.join(DOWNLOADS_PATH, file), destination)
    elif f_ext in EXT_VIDEO:
        for file in f_list:
            destination = os.path.join(BASE_PATH, 'Movies', file)
            if os.path.exists(destination):
                destination = os.path.join(BASE_PATH, 'Movies', f"{file.split('.')[0]}_1.{f_ext}")
            os.rename(os.path.join(DOWNLOADS_PATH, file), destination)
    elif f_ext in EXT_IMGS:
        for file in f_list:
            destination = os.path.join(BASE_PATH, 'Pictures', file)
            if os.path.exists(destination):
                destination = os.path.join(BASE_PATH, 'Pictures', f"{file.split('.')[0]}_1.{f_ext}")
            os.rename(os.path.join(DOWNLOADS_PATH, file), destination)
    elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
        for file in f_list: 
            destination = os.path.join(BASE_PATH, 'Documents', file)
            if os.path.exists(destination):
                destination = os.path.join(BASE_PATH, 'Documents', f"{file.split('.')[0]}_1.{f_ext}")
            os.rename(os.path.join(DOWNLOADS_PATH, file), destination)
    else:
        for file in f_list:
            destination = os.path.join(BASE_PATH, 'Other', file)
            if os.path.exists(destination):
                destination = os.path.join(BASE_PATH, 'Other', f"{file.split('.')[0]}_1.{f_ext}")
            os.rename(os.path.join(DOWNLOADS_PATH, file), destination)