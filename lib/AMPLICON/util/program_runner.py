import subprocess
import os


def run_program(input_file, output_file):
    """
    Run input command
    """
    # define script dir
    script_dir = 'util'
    python_script = os.path.join(script_dir, 'collapse_table.py')
    faprotax_script = os.path.join(script_dir, 'FAPROTAX.txt')

    cmd = ['python', python_script, '-i', input_file,
           '-o', output_file, '-g', faprotax_script, '-v']

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, close_fds=True)

    exitCode = p.wait()

    stream = os.popen('pwd')
    output = stream.read()
    print('***PWD************' + output + '*****************')
    stream = os.popen('ls')
    output = stream.read()
    print('***LS************' + output + '*****************')

    if (exitCode == 0):
        print('\n' + ' '.join(cmd) +
              ' was executed successfully, exit code was: ' + str(exitCode))
    else:
        print('\n' + ' '.join(cmd) +
              ' was fail to execute, exit code was: ' + str(exitCode))

    return exitCode
