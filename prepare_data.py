import os
import sys
from pathlib import Path
import argparse
import pandas as pd
from tqdm import tqdm

all_args = argparse.ArgumentParser(description='Prepare data for training')

# declare the root directory in arguement
all_args.add_argument('--root_dir', type=str, default='')

# declare the output directory in arguement
all_args.add_argument('--output_dir', type=str, default='')

# declare the file whose files need to be kept
all_args.add_argument('--file_list_test', type=str, default='')
all_args.add_argument('--file_list_train', type=str, default='')


def main():
    args = all_args.parse_args()
    root_dir = args.root_dir
    output_dir = args.output_dir
    file_list_train = args.file_list_train
    file_list_test = args.file_list_test

    if not os.path.exists(root_dir):
        print("Root directory doesn't exist")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if not os.path.exists(Path(output_dir)/'train'):
        os.makedirs(Path(output_dir)/'train')
    
    if not os.path.exists(Path(output_dir)/'test'):
        os.makedirs(Path(output_dir)/'test')

    # create a list of all the files in the root directory
    root_list = [Path(root_dir) / folder for folder in os.listdir(root_dir) 
                    if os.path.isdir(Path(root_dir) / folder) and os.path.exists(Path(root_dir) / f"{folder}/audio")]
    paths_list = [ Path(folder) / f"audio/{name}" for folder in root_list for name in os.listdir(folder/"audio") if name.endswith(".wav")]



    # read the file_list_evaluate file
    to_be_kept_train = [ path for path in paths_list if "audio/"+path.name in pd.read_csv(file_list_train, sep="	")["filename"].to_list()]
    to_be_kept_test = [ path for path in paths_list if "audio/"+path.name in pd.read_csv(file_list_test, sep="	")["filename"].to_list()]
    # print("Number of files to be deleted: ", len(to_be_deleted))
    print("Number of files to be kept: ", len(to_be_kept_train)+len(to_be_kept_test))


    # move the to be kept files to the output directory
    print('Moving training files to output directory')
    for path in tqdm(to_be_kept_train):
        os.rename(path, Path(output_dir)/f'train/{path.name}')
    print("Done")

    print('Moving testing files to output directory')
    for path in tqdm(to_be_kept_test):
        os.rename(path, Path(output_dir)/f'test/{path.name}')
    print("Done")


if __name__ == "__main__":
    main()