
import json, os
from extract_keys_recursive import get_keys
from constants import *

def process_files(input_directory):
    files_in_input_directory = os.listdir(input_directory)
    print ("Total files to process = {}".format(len(files_in_input_directory)))

    all_json_keys = list()
    for each_file in files_in_input_directory:
        """
            Some of the json files i was handing did not have correct format,
            so i created a ignore list.
            The latest code has a try except block, to handle the same.
        """
        # if each_file in ignore_file_list:
        #     continue
        # print ("Processing file - {}".format(each_file))
        try:
            file_name_to_process = input_directory + each_file
            with open (file_name_to_process) as json_file:
                json_data = json.load(json_file)
                all_json_keys = get_keys(json_data, all_json_keys)
        except Exception as e:
            print ("Error while processing file - {}".format(file_name_to_process))
            print ("Error message               - {}".format(e))
            print ("-*"*50)
    #         print ("Processing file - {} | Keys in file - {}".format(each_file, len(all_json_keys)))
    #     print ("1. All Keys till here - {}".format(len(all_json_keys)))

    # print ("2. All Keys till here - {}".format(len(all_json_keys)))

    distinct_keys = set(all_json_keys)
    sorted_distinct_keys = sorted(distinct_keys)
    print ("Total Distinct Keys - {}".format(len(sorted_distinct_keys)))

    output_file_ptr = open('output/EMEA_All_Keys.txt', 'w')
    for each_key in sorted_distinct_keys:
        print (each_key, file=output_file_ptr, end='\n')


