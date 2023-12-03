import sys
from pathlib import Path


JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
MY_OTHER = []
ARCHIVES = []
JPEG_IMAGES = []
VIDEO_FILE = []
AVI_VIDEO =[]
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOK_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []



REGISTER_EXTENSION = {
'JPEG': JPEG_IMAGES,
'JPG': JPG_IMAGES,
'PNG': PNG_IMAGES,
'SVG': SVG_IMAGES,
'MP3': MP3_AUDIO,
'ZIP': ARCHIVES,
'AVI': AVI_VIDEO,
'MP4': MP4_VIDEO, 
'MOV': MOV_VIDEO, 
'MKV': MKV_VIDEO,
'DOK': DOK_DOCUMENTS,
'DOCX': DOCX_DOCUMENTS,
'TXT' : TXT_DOCUMENTS,
'PDF' : PDF_DOCUMENTS,
'XLSX' : XLSX_DOCUMENTS,
'PPTX' : PPTX_DOCUMENTS,
'OGG' : OGG_AUDIO,
'WAV' : WAV_AUDIO,
'AMR' : AMR_AUDIO,
'GZ' : ARCHIVES,
'TAR' : ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder:Path):

    for item in folder.iterdir():
       
        if item.is_dir():  # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        
        extension = get_extension(item.name)  
        full_name = folder / item.name  
        if not extension:
          MY_OTHER.append(full_name)
        else:
            try:
                REGISTER_EXTENSION[extension].append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)
if __name__ == "__main__":
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'AUDIO mp3: {MP3_AUDIO}')
    print(f'Archives zip: {ARCHIVES}')
    print(f'Video avi:{AVI_VIDEO}')
    print(f'Video mp4:{MP4_VIDEO}')
    print(f'Video mov:{MOV_VIDEO}')
    print(f'Video mkv:{MKV_VIDEO}')
    print(f'documents dok:{DOK_DOCUMENTS}')
    print(f'documents docx:{DOCX_DOCUMENTS}')
    print(f'documents txt:{TXT_DOCUMENTS}')
    print(f'documents pdf:{PDF_DOCUMENTS}')
    print(f'documents xlsx:{XLSX_DOCUMENTS}')
    print(f'documents pptx:{PPTX_DOCUMENTS}')
    print(f'AUDIO ogg:{OGG_AUDIO}')
    print(f'AUDIO wav:{WAV_AUDIO}')
    print(f'AUDIO amr:{AMR_AUDIO}')
    print(f'Archives gz:{ARCHIVES}')
    print(f'Archives tar:{ARCHIVES}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')

    print("тест")



