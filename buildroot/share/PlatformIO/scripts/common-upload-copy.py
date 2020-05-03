from __future__ import print_function

import os
Import("env")

# please keep $SOURCE variable, it will be replaced with a path to firmware

# Generic
#env.Replace(
#    UPLOADER="executable or path to executable",
#    UPLOADCMD="$UPLOADER $UPLOADERFLAGS $SOURCE"
#)

# In-line command with arguments
#env.Replace(
#    UPLOADCMD="executable -arg1 -arg2 $SOURCE"
#)

# Python callback
def on_upload(source, target, env):
    from shutil import copy

    file_source = str(source[0])
    file_target = env["UPLOAD_PORT"]

    # copy
    copy(file_source, file_target)

env.Replace(UPLOADCMD=on_upload)
