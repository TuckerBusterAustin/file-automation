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
import pathlib

###################################
#       Folder Creation           #
###################################

def folderCheck(lstFolders, rootPath):
    
    for x in lstFolders:
        folder_path = rootPath / x  
        if folder_path.exists(): 
            print(f"Folder path {x} exists")
        else:
            print(f"Folder path {x} does not exist. Creating folder path...")
            folder_path.mkdir(parents=True)

###################################
#              Main               #
###################################

#Folder path initialization
docRoot = Path.home() / 'Documents'
downloadRoot = Path.home() / 'Downloads'
picRoot = Path.home() / 'Pictures'
musicRoot = Path.home() / 'Music'
videoRoot = Path.home() / 'Videos'

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
for root_path in rootPaths:
    allFiles = [x for x in root_path.iterdir()]  # Using pathlib to list files
    
    # Checking all files
    for file_path in allFiles:
        if file_path.is_file():  # Using pathlib to check if it's a file
            ext = file_path.suffix.lower()  # Using pathlib to get the file extension
            
            # The rest of the logic remains the same
            for d in allDicts:
                for key, value in d.items():
                    if ext in value:
                        print(f"Moving file {file_path.name}")
                        shutil.move(str(file_path), str(d['Path'] / key))  # Using pathlib for destination path
