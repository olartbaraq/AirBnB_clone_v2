#!/usr/bin/pyhton3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, 
using the function do_pack
"""

from __future__ import with_statement
from fabric.api import local, settings
from datetime import datetime


def do_pack():
    """function to call the fabfile"""
    local("mkdir -p versions")
    current_time = str(datetime.now())
    current_time = (current_time.split('.'))[0]
    current_time = current_time.replace(':', '')
    current_time = current_time.replace(' ', '')
    current_time = current_time.replace('-', '')
    file_path = 'versions/web_static_' + current_time + '.tgz'
    with settings(warn_only=True):
        result = local("tar -zcvf {} web_static".format(file_path))
    if result.failed:
        return None
    else:
        return file_path
