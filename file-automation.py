"""
File Automation

Description: Automaticallly creates a folder structure and sorts the files in your download
and documents folder and places them in their respective folder

Usage: Run the .exe file to manage new files outside of the folder structure

Author: Brian Sedano
Date: 16/08/2023
Version: 1.2
Dependencies: OS, Shuttle.
"""

import os
import shutil

###################################
#       Folder Creation           #
###################################

def folderCheck(lstFolders,strRootPath):
    
    for x in lstFolders:
        if os.path.exists(strRootPath+x):
           print("Folder path {} exists".format(x))
        else:
            print("Folder path {} does not exist. Creating folder path...".format(x))
            os.makedirs(strRootPath+x)

###################################
#              Main               #
###################################

#Folder path initialization
strDesktopRoot = os.path.expanduser('~/Desktop/')
strDocRoot = os.path.expanduser('~/Documents/')
strDownloadRoot = os.path.expanduser('~/Downloads/')
strPicRoot = os.path.expanduser('~/Pictures/')
strMusicRoot = os.path.expanduser('~/Music/')
strVideoRoot = os.path.expanduser('~/Videos/')

lstRootPaths = [strDocRoot,strDownloadRoot,strPicRoot,strMusicRoot,strVideoRoot]

#Folder Lists
lstDocFolders = ['Word', 'Excel', 'PowerPoint', 'PDF', 'Text File', 'Executables', 'Zip','Other']
lstPictureFolders = ['JPG', 'JPEG', 'PNG', 'GIF', 'BMP']
lstAudioFolders = ['MP3','WAV','Other']
lstVideoFolders = ['MP4','AVI','Other']

#Checking/Creating file structure
folderCheck(lstDocFolders,strDocRoot)
folderCheck(lstPictureFolders,strPicRoot)
folderCheck(lstAudioFolders,strMusicRoot)
folderCheck(lstVideoFolders,strVideoRoot)

#Extention lists
dictDocument = {
    'Path': strDocRoot,
    'Word': ['.docx','.doc'],
    'Excel': ['.xlsx','.xls'],
    'PowerPoint': ['.pptx','.ppt'],
    'PDF': ['.pdf'],
    'Text File': ['.txt','.csv','.rtf','.html','.xml','.json','.md','.psd','.ai','.svg','.htm','.pages','.css',],
    'Executables': ['.exe','.bat','.cmd','.com','.ps1','.vbs','.js','.jar','.py','.sh','.msi','.vs','.c','.s'],
    'Zip': ['.zip','.rar','.7z','.gz','.tar.gz'],
    'Other': ['.webp']
}

dictPictures = {'Path': strPicRoot,'JPG': ['.jpg'], 'JPEG': ['.jpeg'], 'PNG': ['.png'], 'GIF': ['.gif'], 'Other': ['.bmp']}
dictAudio = {'Path': strMusicRoot,'MP3': ['.mp3'], 'WAV': ['.wav'], 'Other': ['.m4a']}
dictVideo = {'Path': strVideoRoot,'MP4': ['.mp4'], 'AVI': ['.avi'], 'Other': ['.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', 
                '.mpg', '.mpeg', '.m4v', '.ts', '.vob', '.rm', '.rmvb', '.asf', '.ogv']}

lstAllDict = [dictDocument,dictPictures,dictAudio,dictVideo]

###################################
#         File Managment          #
###################################

#Checking all paths
for x in lstRootPaths:
    lstAllFiles = os.listdir(x)
    #Checking all files
    for y in lstAllFiles:
        strExt = y[y.rfind('.'):].lower() 
        if len(strExt) >= 2 or len(strExt) >= 4:
            #Checking all Dictionaries
            for z in lstAllDict:
                #All values inside Dictionaries
                for key,value in z.items():
                    #If extention in values of a key, return a key
                    if  strExt in value:
                        print("Moving file {}".format(y))
                        shutil.move(x+y,str(z['Path'])+key)
        else:
            print('File entry is folder. Cannot move')