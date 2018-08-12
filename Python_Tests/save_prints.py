import sys

# Define global variables.
old_stdout = ''
buffer = ''

def start():
    global old_stdout, buffer

    # Save default stdout stream.
    old_stdout = sys.stdout
    
    python_version = sys.version_info[0]
    
    if(python_version == 2):
        import StringIO
        sys.stdout = buffer = StringIO.StringIO()
    elif(python_version == 3):
        import io
        sys.stdout = buffer = io.StringIO()

def stop():
    global old_stdout, buffer

    # Restore default stdout stream.
    sys.stdout = old_stdout

    printed_lines = buffer.getvalue()
    print('\n' + printed_lines)
    return printed_lines.splitlines(True)
