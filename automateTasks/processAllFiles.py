from pathlib import Path
import processFiles

path = Path()

for file in path.glob('*.xlsx'):
    new_file_name = f'{file}-corrected.xlsx'
    processFiles.process_files(file, new_file_name,'sheet1')