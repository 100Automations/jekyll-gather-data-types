# Gather Missing Data Types

## Description
This project was started to automate a way to identify missing data on projact cards for the HackForLA website. The data on these project cards are stored in .md files as collections using YAML syntax.

The `InitDataType.py` script iterates through all .md files in a target directory and creates a set of all data types used accross directory. This set is then used by `GatherMissingDataTypes.py` to generate a spreadsheet with unused and missing data types for each file.

The spreadsheet generated will have two sheets, one to track unused data types and the other to track missing data types. A data type is considered to be unused if that data type is not present at all in that .md file. A data type is considered to be missing if one or more nested data types is not present in the .md file while the root data type is present.

Note: Nested data types are represented by comma seperated entries
For example `one,two,three` would represent
```
one:
    two:
        three: value
```

![Spreadsheet](./images/spreadsheet.png)

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
