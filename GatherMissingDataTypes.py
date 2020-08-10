'''
Generate spreadsheet with unused and missing data types for each file collected by InitDataTypes.py
'''

import os
import yaml
import argparse
import marshal
import sys
from openpyxl import Workbook

def gatherMissingTypes(missingSet, nestedKeyDict, dictionary, prefix, k, v):
    prefixList = (prefix + k).split(",")
    if(nestedKeyDict[prefixList[0]]):
        currentSet = set(dictionary.keys())
        expectedSet = set()
        dataTypeDictionary = dict(nestedKeyDict)
        for key in prefixList:
            dataTypeDictionary = dataTypeDictionary[key]
        expectedSet = set(dataTypeDictionary.keys())
        missingSet.update((expectedSet - currentSet))

def gatherDictionaryKeys(keySet, missingSet, nestedKeyDict, dictionary, prefix):
    for k,v in dictionary.items():
        if(prefix):
            keySet.add(prefix + "," + k)
        else:
            keySet.add(k)

        if type(v) is dict:
            gatherDictionaryKeys(keySet, missingSet, nestedKeyDict, v, prefix + "," + k if prefix else k)
        
        if type(v) is list:
            for item in v:
                if type(item) is dict:
                    gatherMissingTypes(missingSet, nestedKeyDict, item, prefix, k, v)
                    gatherDictionaryKeys(keySet, missingSet, nestedKeyDict, item, prefix + "," + k if prefix else k)

argumentParser = argparse.ArgumentParser(description='Generate spreapsheet with unused and missing data types for each file collected by InitDataTypes.py')
argumentParser.add_argument('-d',
                            metavar='output_directory',
                            type=str,
                            nargs='?',
                            help='Path to output',
                            default='./')

argumentParser.add_argument('-o',
                            metavar='output_name',
                            type=str,
                            nargs='?',
                            help='name for spreadsheetfile -> [output_name].xlsx',
                            default='missingDataTypes')

args = argumentParser.parse_args()

SAVE_PATH = args.d + args.o + '.xlsx'

try:
    marshalFile = open("./dataTypes.marshal", 'rb')
    DIR_PATH = marshal.load(marshalFile)
    USED_DATA_TYPES = marshal.load(marshalFile)
    NESTED_DATA_TYPES = marshal.load(marshalFile)
    marshalFile.close()
except:
    print("Failed to load init information from ./dataTypes.marshal\n")
    sys.exit()

workbook = Workbook()
unusedDataSheet = workbook.active
unusedDataSheet.title = "Unused Data Types"

missingDataSheet = workbook.create_sheet("Missing Data Types")

directory = r'' + DIR_PATH

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

        usedDataTypes = set()
        missingDataTypes = set()
        for dictionary in data:
            if(dictionary):
                gatherDictionaryKeys(usedDataTypes,
                                     missingDataTypes,
                                     NESTED_DATA_TYPES,
                                     dictionary,
                                     "")

        unusedDataTypes = USED_DATA_TYPES - usedDataTypes

        for dataType in unusedDataTypes:
            unusedDataSheet.append([os.path.splitext(filename)[0], dataType])
        
        for missingType in missingDataTypes:
            missingDataSheet.append([os.path.splitext(filename)[0], missingType])

        mdFile.close()

workbook.save(SAVE_PATH)