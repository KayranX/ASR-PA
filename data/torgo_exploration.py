import bz2
import os


def decompress_bz2_file(folder_path: str, file_name: str or None = None, save_decompressed: bool = False):
    # check for the validity of the file_path, raise an error if the path does not exist
    if not os.path.exists(folder_path):
        raise ValueError(
            "The provided folder path is invalid. Please ensure its validity!"
        )

    # iterate through all files in folder, load all files and save them if required
    elif file_name is None:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.bz2'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'rb') as file:
                    compressed_data = file.read()
                decompressed_data = bz2.decompress(compressed_data)
                print(decompressed_data)

    # load specific file from provided folder
    elif file_name.endswith('.bz2'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'rb') as file:
            compressed_data = file.read()
        decompressed_data = bz2.decompress(compressed_data)
        print(decompressed_data)

    # raise an error due to invalid inputs
    else:
        raise ValueError(
            "The provided file name does not have the required format. Please ensure that the file name ends with .bz2!"
        )


if __name__ == '__main__':
    folder_path = "C:/Users/Johan/Documents/Speech Pathology and Recognition/data"
    decompress_bz2_file(folder_path=folder_path, save_decompressed=False)
