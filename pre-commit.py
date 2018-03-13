#!/usr/bin/env python3

import contextlib
import os
import pprint
import subprocess

def get_gradle_root_directory(file_path):
	gradle_file_name = 'build.gradle'
	current_dir = os.path.dirname(file_path)
	end_dir = os.path.join(get_top_level_directory(), 'modules')
	gradle_file_found = False
	count = 0
	while not gradle_file_found and current_dir != end_dir:
		gradle_file_path = os.path.join(current_dir, gradle_file_name)
		gradle_file_found = os.path.exists(gradle_file_path)
		last_dir = current_dir
		current_dir = os.path.dirname(current_dir)

	if gradle_file_found:
		return os.path.dirname(gradle_file_path)
	else:
		return None


def get_top_level_directory():
	completed_process = subprocess.run(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE)
	return completed_process.stdout.decode().strip('\n')


@contextlib.contextmanager
def change_working_dir(new_working_dir):
	current_working_dir = os.getcwd()

	os.chdir(new_working_dir)

	yield

	os.chdir(current_working_dir)


completed_process = subprocess.run(['git', 'diff', '--name-only', '--cached'], stdout=subprocess.PIPE)

directories_to_format = set()

for file_path in completed_process.stdout.decode().split('\n'):
	if file_path:
		directories_to_format.add(get_gradle_root_directory(file_path))

for directory in directories_to_format:
	gradlew_path = os.path.abspath(os.path.join(get_top_level_directory(), 'gradlew'))
	with change_working_dir(directory):
		subprocess.run([gradlew_path, 'formatSource'])

exit(1)
