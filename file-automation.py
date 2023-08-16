"""
File Automation

Description: Automaticallly creates a folder structure and sorts the files in your download
and documents folder and places them in their respective folder

Usage: Run the .exe file to manage new files outside of the folder structure

Author: Brian Sedano
Date: 16/08/2023
Version: 1.0
Dependencies: OS, Shuttle.
"""

import os
import shutil

##########################################################################################################################

def folderPathCheck(strRootFolderPath):
    print("Create folder paths")
    
    lstFolders = ['Document','Image','Audio','Video','Exe','Zip','Folder']

    for x in lstFolders:
        if os.path.exists(strRootFolderPath+x):
            print("Folder path {} exists".format(x))
        else:
            print("Folder path {} does not exist. Creating folder path...".format(x))
            os.makedirs(strRootFolderPath+x)

##########################################################################################################################


def moveFiles(strDirPath, lstDirFiles):
    print("move file")

    StrDocRoot = os.path.expanduser('~/Documents')
    strDocPath = StrDocRoot+'/'+'Automation'+'/'

    lstDocExt = ['.docx','.doc','.xlsx','.xls','pptx','.ppt','.pdf','.txt','.csv','.rtf',
                 '.html','.xml','.json','.md','.psd','.ai','.svg','.webp','.htm','.pages']
    lstImgExt = ['.jpg','.jpeg','.png','.gif','.bmp']
    lstAudioExt = ['.mp3','.wav','.mp4','.mov','.avi','.avi','m4a']
    lstVideoExt = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', 
                   '.mpg', '.mpeg', '.m4v', '.ts', '.vob', '.rm', '.rmvb', '.asf', '.ogv']
    lstExeExt = ['.exe','.bat','.cmd','.com','.ps1','.vbs','.js','.jar','.py','.sh','.msi','.vs','.c']
    lstZipExt = ['.zip','.rar','.7z','.gz','.tar.gz']

    print ("Moving these files: {}".format(lstDirFiles))
    for x in lstDirFiles:
        if any(y in x.lower() for y in lstDocExt):
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Document'+'/')
        if any(y in x.lower() for y in lstImgExt):
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Image'+'/')
        if any(y in x.lower() for y in lstAudioExt):
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Audio'+'/')
        if any(y in x.lower() for y in lstVideoExt):
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Video'+'/')
        if any(y in x.lower() for y in lstExeExt):
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Exe'+'/')
        if any(y in x.lower() for y in lstZipExt):
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Zip'+'/')
        if 'Automation' not in x and '.ini' not in x and 'GitHub' not in x:
            shutil.move(strDirPath+'/'+x, strDocPath+'/'+'Folder'+'/')

##########################################################################################################################

def fileCheck(strDocPath, strDownloadPath):
    print('Check directory files')

    lstDocDirFiles = os.listdir(strDocPath)
    lstDownloadDirFiles = os.listdir(strDownloadPath)
    
    print(lstDocDirFiles)

    for x in lstDownloadDirFiles:
          if x != 'Automation' and x != ' ':
            boolFileExists = True
            if boolFileExists == True:
                moveFiles(strDownloadPath,  lstDownloadDirFiles)
                break

    for x in lstDocDirFiles:
        if x != 'Automation' and x != ' ':
            boolFileExists = True
            if boolFileExists == True:
                moveFiles(strDocPath,  lstDocDirFiles)
                break
    
##########################################################################################################################

def main():
   
   StrDocRoot = os.path.expanduser('~/Documents')
   StrDownloadRoot = os.path.expanduser('~/Downloads')

   print(StrDocRoot)

   oStrDocPath = StrDocRoot+'/'+'Automation'+'/'
   
   folderPathCheck(oStrDocPath)
   fileCheck(StrDocRoot, StrDownloadRoot)

main()