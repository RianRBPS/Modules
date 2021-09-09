# Compress files to take up less space

import zipfile

# Cria e escreve os textos
f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()
f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()

# Cria o arquivo zip
compressed_file = zipfile.ZipFile('compressed_file.zip','w')

# Transfere os textos pro arquivo zip
compressed_file.write('fileone.txt', compress_type = zipfile.ZIP_DEFLATED)
compressed_file.write('filetwo.txt', compress_type = zipfile.ZIP_DEFLATED)
compressed_file.close()

zip_obj = zipfile.ZipFile('compressed_file.zip','r') # Reading method

zip_obj.extractall('extracted_content')

import shutil

output_filename = 'example'


# shutil.make_archive(output_filename, 'zip', dir_to_zip)

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')

