import sys

# Define global variables.
old_stdout = ''
buffer = ''

def start_recording():
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

def stop_recording():
    global old_stdout

    # Restore default stdout stream.
    sys.stdout = old_stdout

def get_prints():
    global buffer

    printed_lines = buffer.getvalue()
    print('\n' + printed_lines)
    return printed_lines.splitlines(True)
