import os
import shutil
import subprocess
import sys


def run_setup(args):
    args.insert(0, 'setup.py')
    args.insert(0, sys.executable)
    process = subprocess.Popen(executable=sys.executable, args=args)
    process.wait()


if __name__ == '__main__':
    for kind in ['rope', 'ropeide']:
        manifest = 'tools/%s_MANIFEST.in' % kind
        setup = 'tools/%s_setup.py' % kind
        shutil.copy(manifest, 'MANIFEST.in')
        shutil.copy(setup, 'setup.py')
        try:
            run_setup(sys.argv[1:])
        finally:
            for temp in ['setup.py', 'MANIFEST.in', 'MANIFEST']:
                if os.path.exists(temp):
                    os.remove(temp)