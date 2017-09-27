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

import os
import subprocess
import sys

expected_num_arguments = 4
if len(sys.argv) == (expected_num_arguments + 1):

    # The -W flag causes the open command to wait until the opened application exits before returning. This is necessary for "git diff" becuase it will delete the temporary files it generates for comparison when this script exits.
    command_args = ['open', '-a', 'p4merge', '-W', '--args']

    for file_path in sys.argv[1:]:
        command_args.append(os.path.abspath(file_path))
    p4merge_exit_status = subprocess.call(command_args)
    sys.exit(p4merge_exit_status)
else:
    print('Error: expected %d arguments; received %d arguments' %
          (expected_num_arguments, (len(sys.argv) - 1)))
    sys.exit(1)
