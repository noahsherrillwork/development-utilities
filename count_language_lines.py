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

total_lines = 0

for (root, dirs, files) in os.walk('liferay-portal'):
    #print(root)
    for file_name in files:
        if file_name == 'Language.properties' and '\\src\\' in root:
            language_file = open(os.path.join(root, file_name))
            language_lines = language_file.readlines()
            for line in language_lines:
                if '=' in line:
                    total_lines += 1
            language_file.close()

print(total_lines)
