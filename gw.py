import os
import subprocess
import sys

sub_command = sys.argv[1]
current_dir = os.getcwd()
gradle_file_name = 'gradlew.bat'
last_dir = ''
command_found = False
while not command_found and current_dir != last_dir:
    last_dir = current_dir
    current_dir = os.path.dirname(current_dir)
    command_path = os.path.join(current_dir, gradle_file_name)
    command_found = os.path.exists(command_path)

if command_found is True:
    subprocess.run([command_path, sub_command])
else:
    print('gradlew command not found')
