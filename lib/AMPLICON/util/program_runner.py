import subprocess


def run_program(input_file, output_file):
    """
    Run input command
    """

    cmd = ['python', 'collapse_table.py', '-i', input_file,
           '-o', output_file, '-g', 'FAPROTAX.txt', '-v']

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, close_fds=True)

    exitCode = p.wait()

    if (exitCode == 0):
        print('\n' + ' '.join(cmd) +
              ' was executed successfully, exit code was: ' + str(exitCode))
    else:
        print('\n' + ' '.join(cmd) +
              ' was fail to execute, exit code was: ' + str(exitCode))

    return exitCode
