import json
import platform
import sys
import yaml
import subprocess

from distutils.sysconfig import get_python_lib


def get_info():
    inf = {}
    inf['version'] = platform.python_version()

    pack = str(subprocess.check_output(["pyenv", "versions"]))
    pack = pack[2:]
    pack = pack.split('\\n')
    pack.pop()
    for i in range(len(pack)):
        pack[i] = pack[i][2:]
    inf['name'] = pack

    pack = str(subprocess.check_output(["virtualenv", "--version"]))
    pack = pack[2:-3]
    inf['virtualenv'] = pack

    inf['exec'] = sys.executable

    pack = str(subprocess.check_output(["pyenv", "which", "pip"]))
    pack = pack[2:-3]
    inf['pip'] = pack

    inf['path'] = sys.path

    pack = str(subprocess.check_output(["pip", "freeze"]))
    lst = pack.split('\\n')
    lst[0] = lst[0][2:]
    lst.pop()
    inf['installed-packages'] = {}
    for i in lst:
        a, b = i.split('==')
        inf['installed-packages'][a] = b
    inf['site-packages'] = get_python_lib()

    return inf


def output_json(inf):
    res = json.dumps({
        'Version': inf['version'],
        'Name': inf['name'],
        'Virtualenv': inf['virtualenv'],
        'Execution location': inf['exec'],
        'Pip': inf['pip'],
        'PYTHONPATH': inf['path'],
        'Installed packages': inf['installed-packages'],
        'Site-packages': inf['site-packages']
        }, indent=4)
    with open("out.json", "w") as f:
        f.write(res + '\n')


def output_yaml(inf):
    res = yaml.dump({
        'Version': inf['version'],
        'Name': inf['name'],
        'Virtualenv': inf['virtualenv'],
        'Execution location': inf['exec'],
        'Pip': inf['pip'],
        'PYTHONPATH': inf['path'],
        'Installed packages': inf['installed-packages'],
        'Site-packages': inf['site-packages']
        }, default_flow_style=False)
    with open("out.yaml", "w") as f:
        f.write(res + '\n')


if __name__ == '__main__':
    info = get_info()
    output_json(info)
    output_yaml(info)
