import os
import subprocess
import sys


usage = """
Usage:

python test_kuma.py [arg]

[arg] is optional; if not specified, runs all tests. If specified, can
take the following forms:

app
    Runs tests in that app.

app.module
    Runs tests in that specific module.

app.module.testcase
    Runs a single specific test case.

app.module.testcase.testname
    Runs a single specific named test.
        """

def run_tests(spec=None):
    cmd, args = get_command_parts()
    if spec is None:
        command =  ' '.join((cmd, args))
    else:
        test_arg = format_spec(spec)
        command =  ' '.join((cmd, test_arg, args))
    subprocess.call(command, shell=True)
    

def get_command_parts():
    here = os.path.dirname(os.path.abspath(__file__))
    cmd = "FORCE_DB=1 %s test" % os.path.join(here, 'manage.py')
    args = "-s --noinput --logging-clear-handlers"
    return (cmd, args)

def format_spec(spec):
    parts = spec.split('.')
    return {1:"%s",
            2: "apps.%s.tests.%s",
            3:"apps.%s.tests.%s:%s",
            4:"apps.%s.tests.%s:%s.%s"}[len(parts)] % tuple(parts)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        print usage
    else:
        run_tests(*sys.argv[1:])

