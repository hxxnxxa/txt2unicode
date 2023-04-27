import argparse
import glob
import os

DEFAULT_FILENAME_R = './labels/256-common-hangul.txt'
DEFAULT_FILENAME_W = './labels/256-common-hangul-ucode.txt'

def generate_lbl_ucode(filename_r, filename_w):

    output_file =  filename_w
    if not os.path.isfile(output_file):
        output_file = open(output_file, 'w')
        output_file.close()

    with open(filename_w, 'wt',encoding='utf-8') as fw:
        with open(filename_r, 'rt', encoding='utf-8') as fr:
            labels = fr.read().splitlines()
                    
            for i in range(len(labels)):
                labels_unicode = (hex(ord(labels[i]))[2:]).upper()
                print(labels_unicode)
                fw.writelines(labels_unicode+'\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--lbl', type=str, dest='filename_r', default=DEFAULT_FILENAME_R, help='')
    parser.add_argument('--lbl-split', type=str, dest='filename_w', default=DEFAULT_FILENAME_W, help='')

    args = parser.parse_args()

    generate_lbl_ucode(args.lbl, args.lbl_split)