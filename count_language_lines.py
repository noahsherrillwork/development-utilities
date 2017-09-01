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
