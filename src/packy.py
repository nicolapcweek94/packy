#!/usr/bin/env python
import argparse
import json
import sys
import utils
import subprocess
import os

version = 'Version 0, Update 0, Build 0, BETA.'

parser = argparse.ArgumentParser(
        description='Packy, the worst package manager around')

parser.add_argument('action', metavar='action',
        nargs='?',
        help='Action (install, remove, version etc)')

parser.add_argument('package', metavar='package',
        nargs='?',
        help='Package name')

parser.add_argument('-r', '--repo',
        help='Repository path')

parser.add_argument('-v', '--version',
        action='store_true', default=False,
        help='Get version info')

args = vars(parser.parse_args())

if args['version']:
    print(version)
    sys.exit(0)

if not args['repo']:
    args['repo'] = 'repo.json'

if (not args['package'] and not args['action'] == 'list') or not args['action']:
    print('Unless you\'re using -v or -h, you might want to pass me a package name and an action to do with it.')
    sys.exit(0)

repo = json.loads(open(args['repo']).read())
basedir = '/home/wasp/packy'
installdir = basedir + '/bin/'
sourcesdir = basedir + '/src/'

try:
    if args['action'] == 'install':
        package = repo[args['package']]
        if package['type'] == 'binary' and package['action'] == 'download': # binary package
            name = utils.store(package['url'], installdir)
            print('Succesfully downloaded ' + name)

        elif package['type'] == 'binary' and package['action'] == 'run': # binary package + run after download
            name = utils.store(package['url'], installdir)
            subprocess.check_call(['chmod', '+x', installdir + name])
            subprocess.check_output(installdir + name)

        elif package['type'] == 'git': # git sources
            subprocess.check_output(['git', 'clone', package['url'], args['package']])
            os.chdir(args['package'])
            subprocess.check_output(package['action'].split(' '))
            os.chdir('..')

        elif package['action'] == 'none':
            print("I have nothing to do here")

    elif args['action'] == 'remove':
        # TODO implement remove
        print('TBI')

    elif args['action'] == 'update':
        # TODO implement update
        print('TBI')

    elif args['action'] == 'sync':
        # TODO implement repo update
        print('TBI')

    elif args['action'] == 'list':
        print(str(len(repo)) + ' package(s) available in the repository:')
        for name in repo:
            print(name + ' by ' + repo[name]['author'] + ', version ' + repo[name]['version'])

    elif args['action'] == 'search':
        print('Found package ' + args['package'] + ', version ' + repo[args['package']]['version'] + ' by ' + repo[args['package']]['author'] + '.')

    elif args['action'] == 'version':
        print('Found available version in the repository: ' + repo[args['package']]['version'])

    else:
        print('Unrecognized action. You should use one of these: \'install\', \'remove\', \'update\', \'sync\', \'list\', \'search\', \'version\'')
        sys.exit(0)

except KeyError:
    print('Package not found')
except subprocess.CalledProcessError:
    print('Something went wrong while trying to install the package. Check the output for errors, please.')
except:
    raise
