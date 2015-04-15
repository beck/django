#!/usr/bin/env python

"""Helper script to update sampleproject's translation catalogs."""

import os
import re
import sys

proj_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(proj_dir, '..', '..', '..')))


def update_translation_catalogs():

    from django.core.management import call_command

    prev_cwd = os.getcwd()

    os.chdir(proj_dir)
    call_command('makemessages')
    call_command('compilemessages')

    # keep the diff friendly - kill 'POT-Creation-Date'
    pofile = os.path.join(proj_dir, 'locale', 'fr', 'LC_MESSAGES', 'django.po')

    with open(pofile) as f:
        content = f.read()
    content = re.sub(
        r'^"POT-Creation-Date.+$\s', '', content, flags=re.MULTILINE)
    with open(pofile, 'w') as f:
        f.write(content)

    os.chdir(prev_cwd)


if __name__ == "__main__":
    update_translation_catalogs()
