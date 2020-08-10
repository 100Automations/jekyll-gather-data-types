# Gather Missing Data Types

## Description
TODO

### Requirements
You need Python 2.x or 3.x to run the script

You will also need the OpenPyXL library installed.
##### With `pip`
`pip install openpyxl`
or 
`pip3 install openpyxl`

You will also need the PyYAML library installed.
`pip install pyyaml`
or 
`pip3 install pyyaml`

### How To Use
We first need to parse all the .md files in target directory and generate a set of used data types. This information will be stored in ./dataTypes.marshal and will be process by GatherMissingDataTypes.py.

#### Generate ./dataTypes.marshal
`python3 InitDataTypes.py [target directory]`

Once the ./dataTypes.marshal file is generated you can run the following to generate .xlsx spreadsheet of files and their unused/missing data types.

#### Generate Missing Data Type Spreadsheet
`python3 GatherMissingDataTypes.py -d [output_directory] -o [output_name]`

If you run this script without the flags the default directory for the output will be your current directory and the file name will be missingDataTypes.xlsx
