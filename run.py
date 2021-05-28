import sys
import ntpath
import os.path
import tempfile
import webbrowser
import shutil


if len(sys.argv)<2:
    input("Expected a command line argument with file path.")
    exit(1)

file_path=sys.argv[1]
file_name=ntpath.basename(file_path)
file_extension=os.path.splitext(file_name)[1]

print(file_path)
print(file_name)
print(file_extension)

# TODO: save file

if file_extension=='.py':
    exec(open(file_path).read())
elif file_extension=='.js':
    # run in broswer
    html='<script src="%s"></script>'%(file_path)
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as browser_file:
        url = 'file://' + browser_file.name
        browser_file.write(html)
        webbrowser.open(url)
elif file_extension=='.java':
    directory=file_path.rstrip(file_name)
    os.chdir(directory)
    os.system('javac -d ./bin *.java')
    if os.path.exists('bin'):
        os.chdir('bin')
        os.system('java %s'%(file_name.rstrip(file_extension)))
        os.chdir('..')
        shutil.rmtree('bin')
        
input("\nPress enter to exit...")
