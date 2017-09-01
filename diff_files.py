#! python
import subprocess
import sys

expected_num_arguments = 7
if len(sys.argv) == (expected_num_arguments + 1):
    p4merge_path = 'C:/Program Files/perforce/p4merge'
    old_file_path = sys.argv[2]
    new_file_path = sys.argv[5]
    p4merge_exit_status = subprocess.call([p4merge_path, old_file_path, new_file_path])
    sys.exit(p4merge_exit_status)
else:
    print('Error: expected %d arguments; received %d arguments' %
          (expected_num_arguments, (len(sys.argv) - 1)))
    sys.exit(1)
