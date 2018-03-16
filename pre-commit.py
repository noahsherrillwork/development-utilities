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
import re
import subprocess

class SourceFormatterResult:
	def __init__(self, formatted_dir, output):
		self.formatted_dir = formatted_dir
		self.output = output


def execute_pre_commit_check():
	dirs_to_format = get_dirs_to_format()
	source_formatter_results = run_source_formatter(dirs_to_format)

	if has_any_formatting_errors(source_formatter_results):
		exit('Please fix source formatting errors before committing. Alternatively, you can bypass the automatic execution of source formatter by passing the "--no-verify" option to "git commit"')


def get_dirs_to_format():
	completed_process = subprocess.run(['git', 'diff', '--name-only', '--cached'], stdout=subprocess.PIPE)
	dirs_to_format = set()

	for file_path in completed_process.stdout.decode().split('\n'):
		if file_path and is_java_file(file_path):
			dirs_to_format.add(get_gradle_root_dir(file_path))

	return dirs_to_format


def run_source_formatter(dirs_to_format):
	source_formatter_results = []

	for dir_to_format in dirs_to_format:
		gradlew_path = os.path.abspath(os.path.join(get_top_level_dir(), 'gradlew'))

		with change_working_dir(dir_to_format):
			completed_process = subprocess.run([gradlew_path, 'formatSource'], stdout=subprocess.PIPE)
			source_formatter_output = completed_process.stdout.decode()
			print(source_formatter_output)
			source_formatter_results.append(SourceFormatterResult(dir_to_format, source_formatter_output))

	return source_formatter_results


def has_any_formatting_errors(source_formatter_results):
	return any([has_formatting_errors(source_formatter_result) for source_formatter_result in source_formatter_results])


def get_gradle_root_dir(start_path):
	return get_ancestor_dir_with_file(start_path, 'build.gradle')


def has_formatting_errors(source_formatter_result):
	pattern = (
		r': '			# Error messages are followed by these characters
		r'([./\\\w]+)'	# Relative path for file in which error occurred
		r'\s'			# White space following file path
	)

	match = re.search(pattern, source_formatter_result.output)
	if match:
		relative_file_path = match.group(1)

		if is_valid_formatted_file_path(source_formatter_result.formatted_dir, relative_file_path):
			return True

	return False


def is_valid_formatted_file_path(formatted_dir, relative_file_path):
	return os.path.exists(os.path.join(formatted_dir, relative_file_path))


def is_java_file(file_path):
	return os.path.splitext(file_path)[1] == '.java'


@contextlib.contextmanager
def change_working_dir(new_working_dir):
	current_working_dir = os.getcwd()
	os.chdir(new_working_dir)

	yield

	os.chdir(current_working_dir)


def get_ancestor_dir_with_file(start_dir, file_name):
	file_found = False
	current_dir = start_dir
	end_dir = os.path.join(get_top_level_dir(), 'modules')

	while not file_found and current_dir != end_dir:
		file_check_path = os.path.join(current_dir, file_name)
		file_found = os.path.exists(file_check_path)
		current_dir = os.path.dirname(current_dir)

	if file_found:
		return os.path.dirname(file_check_path)
	else:
		return None


def get_top_level_dir():
	completed_process = subprocess.run(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE)
	return completed_process.stdout.decode().strip('\n')


if __name__ == '__main__':
	execute_pre_commit_check()
