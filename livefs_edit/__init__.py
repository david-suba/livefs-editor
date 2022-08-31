#

import subprocess


def run(cmd, check=True, **kw):
    print(cmd)
    return subprocess.run(cmd, check=check, **kw)


def run_capture(cmd, **kw):
    return run(
        cmd, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        **kw)
