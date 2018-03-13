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
import pprint

def getLanguageCode(fileName):
	fileNameParts = os.path.splitext(fileName)
	fileRootNameParts = fileNameParts[0].partition('_')
	return fileRootNameParts[2]


languageCodes = set()
for (root, _, files) in os.walk('.'):
	for fileName in files:
		if fileName.startswith('Language_'):
			languageCodes.add(getLanguageCode(fileName))

print(len(languageCodes))
with open('language_list.txt', 'w') as languageListFile:
	languageListFile.write(pprint.pformat(languageCodes))
