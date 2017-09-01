# Copyright (c) 2000-present Liferay, Inc. All rights reserved.
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.

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
