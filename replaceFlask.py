#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def replace_dir_name(root_dir, old_str, new_str):
    for dir_path, dir_names, file_names in os.walk(root_dir, topdown = False):
        for dir_name in dir_names:
            if old_str == dir_name:
                dir_name_old = os.path.join(dir_path, dir_name)
                dir_name_new = os.path.join(dir_path, dir_name.replace(old_str, new_str))
                os.system('mv ' + dir_name_old + ' ' + dir_name_new)


def replace_file_name(root_dir, old_str, new_str):
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for file_name in file_names:
            if old_str in file_name:
                file_name_old = os.path.join(dir_path, file_name)
                file_name_new = os.path.join(dir_path, file_name.replace(old_str, new_str))
                os.system('mv ' + file_name_old + ' ' + file_name_new)


def replace_file_content(root_dir, old_str, new_str):
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for file_name in file_names:
            file_obj = os.path.join(dir_path, file_name)
            f = open(file_obj, 'r+')
            all_the_lines = f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                f.write(line.replace(old_str, new_str))


if __name__ == '__main__':
    # replace_file_content('./server', 'server', 'test_project')
    replace_dir_name('./server/', 'server', 'test_project')
