#!/usr/bin/env python
import StringIO
import requests
import os
import os.path
import re
import stat
import sys
import zipfile
import logging


VERSION_URL = 'https://appengine.google.com/api/updatecheck'
DOWNLOAD_URL = [
    'http://googleappengine.googlecode.com/files/google_appengine_{0}.zip',
    'https://commondatastorage.googleapis.com/appengine-sdks/featured/'
    'google_appengine_{0}.zip']
NOTES_URL = 'https://code.google.com/p/googleappengine/wiki/SdkReleaseNotes'


try:
    dest = sys.argv[1]
except IndexError:
    logging.error('please, specify an installation path')
    exit(1)

version_data = requests.get(VERSION_URL).content
version = re.match('release: "([\d\.]+)"', version_data).group(1)
sdk_path = os.path.join(dest, 'google_appengine')
version_file = os.path.join(sdk_path, 'VERSION')
notes_file = os.path.join(sdk_path, 'RELEASE_NOTES')

if os.path.exists(version_file):
    version_data = open(version_file).readline()
    current_version = re.match('release: "([\d\.]+)"', version_data)
    if current_version and current_version.group(1) == version:
        logging.warning('current version of SDK is already installed')
        exit()

logging.warning('fetching new {0} version of GAE SDK'.format(version))
for url in DOWNLOAD_URL:
    sdk_url = url.format(version)
    logging.warning('trying url {0}'.format(sdk_url))
    response = requests.get(sdk_url)
    if response.status_code == 200:
        if os.path.exists(version_file):
            import shutil
            logging.warning('removing old version of %s' % sdk_path)
            shutil.rmtree(sdk_path)
        zipfile.ZipFile(
            StringIO.StringIO(
                response.content)
            ).extractall(path=dest)
        all_x = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        for name in [name for name in os.listdir(sdk_path)
                     if name.endswith('.py')]:
            full_name = os.path.join(sdk_path, name)
            new_mode = os.stat(full_name).st_mode | all_x
            os.chmod(full_name, new_mode)
        logging.warning('release notes: {0}'.format(NOTES_URL))
        release_notes = re.search('{0}(.*?)Version'.format(version),
                                  open(notes_file).read(),
                                  re.DOTALL)
        if release_notes and release_notes.group(1):
            logging.warning(release_notes.group(1))
        logging.warning('done')
        exit()
    else:
        logging.error('cannot fetch url {0} because of HTTP{1} error'.format(
                      url, response.status_code))
