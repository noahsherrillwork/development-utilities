#! python

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
