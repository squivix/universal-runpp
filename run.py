import sys
import ntpath
import os.path
import tempfile
import webbrowser
import shutil
import traceback

def main():
    if len(sys.argv) < 2:
        input("Expected a command line argument with file path.")
        exit(1)

    file_path = sys.argv[1]
    file_name = ntpath.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    print(file_path)
    print(file_name)
    print(file_extension)

    # TODO save file

    if file_extension == '.py':
        run_python(file_path)
    elif file_extension == '.js':
        run_javascript(file_path, True)
    elif file_extension == '.java':
        run_java(file_path, file_name)
    input("\nPress enter to exit...")


def run_python(file_path):
    try:
        exec(open(file_path).read())
    except Exception as e:
        input(traceback.format_exc())


def run_javascript(file_path, run_in_browser=False):
    if run_in_browser:
        html = f'<script src="{file_path}"></script>'
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as browser_file:
            url = 'file://' + browser_file.name
            browser_file.write(html)
            webbrowser.open(url)
    else:
        # run in node.js
        os.system(f'node "{file_path}"')


def run_java(file_path, file_name):
    directory = file_path.rstrip(file_name)
    os.chdir(directory)
    os.system('javac -d ./bin *.java')
    if os.path.exists('bin'):
        os.chdir('bin')
        os.system(f'java {file_name.rstrip(".java")}')
        os.chdir('..')
        shutil.rmtree('bin')

if __name__ == "__main__":
    main()  
