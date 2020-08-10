'''
Parses .md files in [target_directory]
Collects data types used in YAML .md files and stores them in ./dataTypes.marshal 
./dataTypes.marshal is required by GatherMissingDataTypes.py.
'''

import os
import yaml
import argparse
import marshal
import sys

def gatherDictionaryKeys(keySet, dictionary, prefix):
    for k,v in dictionary.items():
        if(prefix):
            keySet.add(prefix + "," + k)
        else:
            keySet.add(k)

        if type(v) is dict:
            gatherDictionaryKeys(keySet, v, prefix + "," + k if prefix else k)
        
        if type(v) is list:
            for item in v:
                if type(item) is dict:
                    gatherDictionaryKeys(keySet, item, prefix + "," + k if prefix else k)

def generateNestedDictionary(keySet):
    nestedDictionary = dict()
    for key in keySet:
        if("," in key):
            keyList = key.split(",")
            currentDictionary = nestedDictionary
            for item in keyList:
                if item in currentDictionary.keys():
                    currentDictionary = currentDictionary[item]
                else:
                    currentDictionary[item] = dict()
                    currentDictionary = currentDictionary[item]
    
    return nestedDictionary

argumentParser = argparse.ArgumentParser(description='Gather used data types in .md files of a directory')
argumentParser.add_argument('TargetDirectory',
                            metavar='target_directory',
                            type=str,
                            help='directory that will be parsed')

args = argumentParser.parse_args()

DIR_PATH = args.TargetDirectory
directory = r'' + DIR_PATH

if not os.path.isdir(DIR_PATH):
    print('The path specified does not exist')
    sys.exit()

usedDataTypes = set()

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        try:
            mdFile = open(DIR_PATH + filename, 'r')
        except:
            print("Failed to open " + filename + "\n")
            continue
        try:
            data = yaml.load_all(mdFile)
        except:
            print("yaml failed to parse " + filename + "\n")
            mdFile.close()
            continue
        for dictionary in data:
            if(dictionary):
                gatherDictionaryKeys(usedDataTypes,dictionary,"")

        mdFile.close()

nestedDictionary = generateNestedDictionary(usedDataTypes)

try:
    storageFile = open("./dataTypes.marshal", 'wb')
    marshal.dump(DIR_PATH, storageFile)
    marshal.dump(usedDataTypes, storageFile)
    marshal.dump(nestedDictionary, storageFile)
    storageFile.close()
except:
    print("Failed to store data type information in ./dataTypes.marshal")
    sys.exit()