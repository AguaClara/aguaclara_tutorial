import sys

# Define global variables.
old_stdout = ''
buffer = ''

def start():
    global old_stdout, buffer

    # Save default stdout stream.
    old_stdout = sys.stdout

    if(get_python_version() == 2):
        import StringIO
        sys.stdout = buffer = StringIO.StringIO()
    elif(get_python_version() == 3):
        import io
        sys.stdout = buffer = io.StringIO()

def stop():
    global old_stdout, buffer

    # Restore default stdout stream.
    sys.stdout = old_stdout

    printed_lines = buffer.getvalue()
    print('\n' + printed_lines)
    return printed_lines.splitlines(True)

def get_python_version():
    return sys.version_info[0]