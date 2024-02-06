import os
import zipfile

def compress(path_to_zip='.', zip_file='output.zip'):
    """지정된 경로를 압축 파일로 만듦."""
    try:
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as ziph:
            for root, dirs, files in os.walk(path_to_zip):
                for file in files:
                    file_path = os.path.join(root, file)
                    ziph.write(file_path, os.path.relpath(file_path, path_to_zip))
        print(f"Compressed {path_to_zip} into {zip_file}")
    except Exception as e:
        print(f"Compression failed: {e}")
        
def extract_all(zip_file='output.zip', path_to_extract='.'):
    """압축 파일을 지정된 경로에 압축 해제."""
    if not zip_file.endswith('.zip'):
        print("This is not a zip file")
        return
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(path_to_extract)
            print(f"Extracted all into {path_to_extract}")
    except zipfile.BadZipFile:
        print("The file is not a zip file or a corrupted zip file.")
    except Exception as e:
        print(f"Unzip has failed: {e}")