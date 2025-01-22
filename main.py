
# sample input to run the project 
# to expand the JSON 
# python main.py --dir input/some_dir --outfile Some_output_file --expand yes
#
# to search the JSON 
# python main.py --dir input/some_dir --search-string someString --search yes
#

import argparse
from load_json import process_files



if __name__ == '__main__':
    #
    # read and process arguments
    #
    argument_parser = argparse.ArgumentParser(description='Json parser, to get unique keys across multiple jsons')
    argument_parser.add_argument('--dir', 
                                type=str, 
                                # required=True, 
                                help='Directory where input json files are present')
    argument_parser.add_argument('--outfile', 
                                type=str, 
                                # required=True, 
                                help='Output file name, do not add extention',
                                default='default')
    argument_parser.add_argument('--expand',
                                 type=str, 
                                # '--extract',
                                # required=True, 
                                help='Option to expand keys')
    argument_parser.add_argument('--search',
                                 type=str, 
                                # '--search',
                                # required=True, 
                                help='Option to search for keys in all json files')
    argument_parser.add_argument('--search-string', 
                                type=str,
                                # required=True, 
                                help='Option to search for keys in all json files')
    
    
    arguments = vars(argument_parser.parse_args())
    # print (arguments)
    # # print (arguments['dir'])
    # input()

    expand_json = False
    search_json = False
    if arguments.get('expand'):
        expand_json = True if arguments.get('expand')[0].casefold() == 'y' else False
    
    if arguments.get('search'):
        search_json = True if arguments.get('search')[0].casefold() == 'y' else False
    
    # print (search_json, expand_json)
    # input()

    if not search_json and not expand_json:
        raise Exception ("Set either --search or expand flag to Yes.")


    if arguments.get('dir'):
        # If the directory name ends in '/' then use that, else add '/' to input directory name
        input_directory = arguments['dir'] if arguments['dir'][-1] == '/' else arguments['dir'] + '/'
    else:
        raise Exception ("Mandatory parameter '--dir' is missing.")

    output_file_ptr = None
    if expand_json:
        if arguments.get('outfile') and not arguments['outfile'] == 'default':
            # If the directory name ends in '/' then use that, else add '/' to input directory name
            out_file_name = 'output/' + arguments['outfile'].replace(' ', '_').replace('.', '_') + '.txt'
            output_file_ptr = open(out_file_name, 'w')
            # input("Out file opened")
        else:
            raise Exception ("Mandatory parameter '--outfile' is missing.")
    
    search_keys = ''
    if search_json:
        if arguments.get('search-string'):
            search_keys = arguments['search-string']

    # print (search_json, search_keys)
    # input()
    process_files(input_directory, output_file_ptr, search_json, search_keys, expand_json)
    


