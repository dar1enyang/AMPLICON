import json
import csv


def parse_input_file(input_file, output_file):
    """
    Convert amplicon data set into tsv
    """

    with open(input_file) as json_file:
        input_data = json.load(json_file)

    tsv_filename = output_file

    with open(tsv_filename, 'w') as tsvfile:

        file_writer = csv.writer(tsvfile, delimiter='\t')

        header = input_data['data']['col_ids']
        header.insert(0, 'taxonomic_id')
        file_writer.writerow(header)

        for i in range(len(input_data['data']['row_ids'])):

            row = input_data['data']['values'][i]
            row.insert(0, input_data['data']['row_ids'][i])
            file_writer.writerow(row)


def parse_input_data(input_data, output_file):
    """
    Convert amplicon data set into tsv
    """

    tsv_filename = output_file

    with open(tsv_filename, 'w') as tsvfile:

        file_writer = csv.writer(tsvfile, delimiter='\t')

        header = input_data['data']['col_ids']
        header.insert(0, 'taxonomic_id')
        file_writer.writerow(header)

        for i in range(len(input_data['data']['row_ids'])):

            row = input_data['data']['values'][i]
            row.insert(0, input_data['data']['row_ids'][i])
            file_writer.writerow(row)
