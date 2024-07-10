import shutil
from pathlib import Path

# https://pypi.org/project/pillow/
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


SOURCE_DIR = r"/Users/emojiestore/Library/Mobile Documents/com~apple~CloudDocs/Обучение ИТ/my_foto"
DIST_DIR = "data"
IMG_NAME = "image.webp"

source_file = Path(SOURCE_DIR).joinpath(IMG_NAME)
copy_file = Path(DIST_DIR).joinpath(IMG_NAME)

# shutil.copy2(src=source_file, dst=copy_file)  # todo reserch about follow_symlinks



# Відкриваємо зображення
image = Image.open(copy_file)

# Отримуємо EXIF-метадані
exif_data = image._getexif()
print(f"{exif_data=}")
if exif_data is not None:
    # Перетворюємо теги EXIF у читабельний формат
    exif = {
        TAGS.get(tag): value
        for tag, value in exif_data.items()
        if tag in TAGS
    }

    # Виводимо всі EXIF-метадані
    for tag, value in exif.items():
        print(f"{tag}: {value}")
else:
    print("Немає EXIF-даних у зображенні")