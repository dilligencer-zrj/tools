# 拷贝每个子文件夹下前N个文件到另一个文件夹下

import os
import sys
import argparse

parser = argparse.ArgumentParser(description='copy tool config')

parser.add_argument(
    '--src_dir',
    type=str,
    default='',
    help='source directory'
)

parser.add_argument(
    '--dst_dir',
    type=str,
    default='',
    help='destination directory'
)

parser.add_argument(
    '--topN',
    type=int,
    default=10,
    help='topN files needed to copy from source directory to destination directory'
)

def copy_topN_file(args):
    subfolders = os.listdir(args.src_dir)
    for subfolder in subfolders:
        src_subfolder = os.path.join(args.src_dir,subfolder)
        dst_subfolder = os.path.join(args.dst_dir,subfolder)
        if not os.path.exists(dst_subfolder):
            os.makedirs(dst_subfolder)
        os.system('cd %s && ls |head -n %d |xargs -i cp {} %s' % (src_subfolder, args.topN, dst_subfolder))

def main():
    args = parser.parse_args ( )
    copy_topN_file(args)

if __name__ == '__main__':
    main()
