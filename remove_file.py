#!/usr/bin/python3
import os
import sys

def get_paths(domain):
    base_path = f'/var/www/html/{domain}/public'
    paths = [f'{base_path}/home/.test',
             f'{base_path}/etc/.test',
             f'{base_path}/root/.test',
             f'{base_path}/usr/local/.test']
    return paths

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a domain name as an argument.')
        sys.exit(1)

    domain = sys.argv[1]
    paths = get_paths(domain)

    for path in paths:
        os.remove(path)