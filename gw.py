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

import contextlib
import os
import subprocess
import sys

def execute():
	command = sys.argv[1]
	if command == 'prModuleCheck':
		run_pr_module_check()
	else:
		with move_settings_file():
			run_gradle_command(command)


def run_pr_module_check():
	with move_settings_file():
		run_gradle_command('formatSource')
		run_gradle_command('pmdMain')
		run_gradle_command('pmdTest')


def run_gradle_command(command):
	gradle_path = os.path.join(get_top_level_directory(), 'gradlew')
	subprocess.run([gradle_path, command])


@contextlib.contextmanager
def move_settings_file():
	settings_path = find_settings_file()

	if settings_path:
		os.rename(settings_path, settings_path + '.tmp')

	yield

	if settings_path:
		os.rename(settings_path + '.tmp', settings_path)


def find_settings_file():
	settings_name = 'settings.gradle'
	current_dir = os.getcwd()
	end_dir = os.path.join(get_top_level_directory(), 'modules')
	settings_found = False
	while not settings_found and current_dir != end_dir:
		settings_path = os.path.join(current_dir, settings_name)
		settings_found = os.path.exists(settings_path)
		last_dir = current_dir
		current_dir = os.path.dirname(current_dir)

	if settings_found:
		return settings_path
	else:
		return None


def get_top_level_directory():
	completed_process = subprocess.run(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE)
	return completed_process.stdout.decode().strip('\n')


if __name__ == '__main__':
	execute()
