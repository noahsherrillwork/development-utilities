#! python
import subprocess
import sys

expected_num_arguments = 4
if len(sys.argv) == (expected_num_arguments + 1):
    p4merge_path = 'C:/Program Files/perforce/p4merge'
    command_args = [p4merge_path]
    command_args.extend(sys.argv[1:])
    p4merge_exit_status = subprocess.call(command_args)
    sys.exit(p4merge_exit_status)
else:
    print('Error: expected %d arguments; received %d arguments' %
          (expected_num_arguments, (len(sys.argv) - 1)))
    sys.exit(1)
