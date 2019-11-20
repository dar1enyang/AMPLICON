import os
import uuid
from .amplicon_output import create_html_tables
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.KBaseReportClient import KBaseReport


def create_report(callback_url, scratch, workspace_name, result_file):

    html = create_html_tables(result_file)

    dfu = DataFileUtil(callback_url)
    report_name = 'fastANI_report_' + str(uuid.uuid4())
    report_client = KBaseReport(callback_url)
    html_dir = os.path.join(scratch, report_name)
    os.mkdir(html_dir)

    with open(os.path.join(html_dir, "index.html"), 'w') as file:
        file.write(html)

    shock = dfu.file_to_shock({
        'file_path': html_dir,
        'make_handle': 0,
        'pack': 'zip'
    })
    html_file = {
        'shock_id': shock['shock_id'],
        'name': 'index.html',
        'label': 'html_files',
        'description': 'FastANI HTML report'
    }
    report = report_client.create_extended_report({
        'direct_html_link_index': 0,
        'html_links': [html_file],
        'report_object_name': report_name,
        'workspace_name': params['workspace_name']
    })

    return {
        'report_name': report['name'],
        'report_ref': report['ref']
    }
