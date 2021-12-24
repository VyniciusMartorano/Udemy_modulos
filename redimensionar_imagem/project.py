import os
from PIL import Image

def main(main_images_folder, new_width=1920):
    if not os.path.isdir(main_images_folder):
         raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)    #extension = pegar a extensao do arquivo
            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension

            new_file_full_path = os.path.join(root,new_file)

            if converted_tag in file_full_path:
                continue

            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size

            new_heigth = round((new_width * height) / width)

            new_image = img_pillow.resize(new_width, new_heigth, Image.LANCZOS)
            new_image.save(new_file_full_path, optimize=True, quality=70)
            new_image.close()
            img_pillow.close()



if __name__ == '__main__':
    main_images_folder = r'C:\Users\vynic\Pictures\imagens'
    main(main_images_folder, 640)