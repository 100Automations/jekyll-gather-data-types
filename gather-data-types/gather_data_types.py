from process_collection import ProcessCollection
from process_dictionary import ProcessDictionary
from spreadsheet import Spreadsheet
import argparse
import json

def gather_collection_data_types(target_directory):
    pc = ProcessCollection(target_directory)
    pc.gather_used_types()
    pc.export_marshal_data()

def json_data_types_report():
    pc = ProcessCollection()
    pc.import_marshal_data()

    return json.loads(pc.gather_missing_unused_data_types())

def spreadsheet_data_types_report(output_directory = './', output_name = 'data-types'):
    pc = ProcessCollection()
    pc.import_marshal_data()

    json_dict = json.loads(pc.gather_missing_unused_data_types())

    spreadsheet = Spreadsheet(output_directory, output_name)
    spreadsheet.json_to_spreadsheet(json_dict)

if __name__ == '__main__':
    argumentParser = argparse.ArgumentParser(description='Generate spreadsheet or json of data types used and missing from jekyll collection')
    argumentParser.add_argument('-x',
                                action='store_true',
                                help='Enables spreadsheet output (.xlsx)')

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
                                default='data-types')
    
    argumentParser.add_argument('-i',
                            metavar='target_directory',
                            type=str,
                            nargs='?',
                            help='directory of jekyll collection to be parsed',
                            default=None)

    argumentParser.add_argument('-j', 
                                action='store_true',
                                help='Enables JSON output')

    args = argumentParser.parse_args()

    if args.i:
        gather_collection_data_types(args.i)
    elif args.j:
        print(json_data_types_report())
    elif args.x:
        spreadsheet_data_types_report(args.d, args.o)