#!/usr/bin/env python3

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

def get_words(line):
	line_parts = line.split('=')
	words = line_parts[1].split(' ')
	return words


def get_unique_words(words):
	unique_words = set()
	for word in words:
		unique_words.add(word.lower())

	return unique_words


total_lines = 0
words = []

for (root, dirs, files) in os.walk('.'):
	print(root)
	for file_name in files:
		src_path_component = os.sep + 'src' + os.sep
		if file_name == 'Language.properties' and src_path_component in root:
			language_file = open(os.path.join(root, file_name))
			language_lines = language_file.readlines()
			for line in language_lines:
				if '=' in line:
					total_lines += 1
					words.extend(get_words(line))
			language_file.close()

print('Total lines = %d' % total_lines)
print('Total words = %d' % len(words))

unique_words = get_unique_words(words)

print('Total unique words = %d' % len(unique_words))
