#!/usr/bin/env python
import argparse, json, sys

version = 'Version 0, Update 0, Build 0, BETA.'

parser = argparse.ArgumentParser(description='Packy, the worst package manager around')

parser.add_argument('action', metavar='action',
        nargs='?',
        help='Action (install, remove, version etc)')

parser.add_argument('packages', metavar='package',
        nargs='?',
        help='Package(s) name')

parser.add_argument('-r','--repo',
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

if (not args['packages'] and not args['action'] == 'list') or not args['action']:
    print('Unless you\'re using -v or -h, you might want to pass me a package name and an action to do with it.')
    sys.exit(0)

repo = json.loads(open(args['repo']).read())

if args['action'] == 'install':
    #TODO implement install
    print('TBI')
elif args['action'] == 'remove':
    #TODO implement remove
    print('TBI')
elif args['action'] == 'list':
    try:
        print(str(len(repo)) + ' package(s) available in the repository:')
        for name in repo:
            print(name + ' by ' +  repo[name]['author'] + ', version ' + repo[name]['version'])
    except:
        raise
elif args['action'] == 'search':
    try:
        print('Found package ' + args['packages'] + ', version ' + repo[args['packages']]['version'] + ' by ' + repo[args['packages']]['author'] + '.')
    except KeyError:
        print('Package not found in the repository')
    except:
        raise
elif args['action'] == 'version':
    try:
        print('Found available version in the repository: ' + repo[args['packages']]['version'])
    except KeyError:
        print('Package not found in the repository.')
    except:
        raise
else:
    print('Unrecognized action. You should use one of these: \'install\', \'remove\', \'list\', \'search\', \'version\'')
    sys.exit(0)
