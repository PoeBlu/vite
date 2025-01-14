import argparse
import sys
from vite import vite
from huepy import *
from vite import __version__


def main():
    desc = green('A simple and minimal static site generator.')
    usage = lightblue('vite') + ' [options]'
    parser = argparse.ArgumentParser(description=desc, usage=usage)
    parser.add_argument('-v', '--version', action='version', version='{version}'.format(version=__version__))
    sp = parser.add_subparsers(dest='cmd', help='Options to help create, build and serve your project.')
    spp = sp.add_parser('new')
    for cmd in ['build', 'serve']:
        sp.add_parser(cmd)
    spp.add_argument('path')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    elif args.cmd == 'new':
        if args.path:
            vite.create_project(args.path)
        else:
            parser.print_help()
    elif args.cmd == 'build':
        vite.import_config()
        vite.builder()
    elif args.cmd == 'serve':
        vite.import_config()
        vite.server()
    else:
        parser.print_help()
