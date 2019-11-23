#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def replaceDirName(rootDir, oldStr, newStr):
    for dirpath, dirNames, fileNames in os.walk(rootDir, topdown = False):
        for dirName in dirNames:
            if oldStr == dirName:
                dirNameOld = os.path.join(dirpath, dirName)
                dirNameNew = os.path.join(dirpath, dirName.replace(oldStr, newStr))
                os.system('mv ' + dirNameOld + ' ' + dirNameNew)


def replaceFileName(rootDir, oldStr, newStr):
    for dirpath, dirNames, fileNames in os.walk(rootDir):
        for fileName in fileNames:
            if oldStr in fileName:
                fileNameOld = os.path.join(dirpath, fileName)
                fileNameNew = os.path.join(dirpath, fileName.replace(oldStr, newStr))
                os.system('mv ' + dirNameOld + ' ' + dirNameNew)


def replaceFileContent(rootDir, oldStr, newStr):
    for dirpath,dirNames,fileNames in os.walk(rootDir):
        for fileName in fileNames:
            fileObj = os.path.join(dirpath, fileName)
            f = open(fileObj, 'r+')
            all_the_lines=f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                f.write(line.replace(oldStr, newStr))


if __name__ == '__main__':
    replaceFileContent('./server', 'server', 'heihei')
    replaceDirName('./server/', 'server', 'heihei')
