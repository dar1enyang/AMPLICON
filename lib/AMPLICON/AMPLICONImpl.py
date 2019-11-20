# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.WorkspaceClient import Workspace

from .util.amplicon_input import parse_input_data
from .util.program_runner import run_program
from .util.amplicon_report import create_report
#END_HEADER


class AMPLICON:
    '''
    Module Name:
    AMPLICON

    Module Description:
    A KBase module: AMPLICON
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']

        self.ws_url = config['workspace-url']
        self.ws_client = Workspace(self.ws_url)

        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass

    def run_AMPLICON(self, ctx, params):

        # ctx is the context object
        # return variables are: output
        #BEGIN run_AMPLICON
        print('Starting AMPLICON function and validating parameters.')
        if not params.get('workspace_name'):
            print('Parameters provided were', str(params))
            raise TypeError('Must pass a non-empty `workspace_name` arg.')
        if not params.get('ref'):
            print('Parameters provided were', str(params))
            raise TypeError('Must pass a non-empty `ref` arg.')

        ws_name = params['workspace_name']
        # get the amplicon data
        obj = self.ws_client.get_objects2({
            'objects': [{'ref': params['ref']}]
        })['data'][0]['data']

        # define file names
        parse_out_file = 'parse_out.tsv'

        input_file = parse_out_file
        output_file = 'output.tsv'

        # 1. convert data into tsv format
        parse_input_data(obj, parse_out_file)

        # 2. run subprocess FAPROTAX
        run_program(input_file, output_file)

        # 3. create html tables using output_file
        output = create_report(self.callback_url, self.shared_folder,
                               ws_name, output_file)

        #END run_AMPLICON

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_AMPLICON return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
