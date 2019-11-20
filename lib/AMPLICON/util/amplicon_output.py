import pandas as pd
import io


def create_html_tables(data_file):
    """
    Import tsv file to generate html tables
    """

    str_io = io.StringIO()
    df = pd.read_csv(data_file, sep='\t', header=0)
    df.to_html(buf=str_io, classes='table table-striped')
    html_str = str_io.getvalue()

    return html_str
