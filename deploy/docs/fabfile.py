# -*- coding: utf-8 -*-

import os
import re
import datetime

# import django
# from django.core.exceptions import AppRegistryNotReady
from fabric.api import local, env, lcd, put, run, cd, task
from fabric.contrib import project
# from fabvenv import virtualenv

HERE = os.path.abspath(os.path.dirname(__file__))
env.hosts = ['root@114.55.86.150']
env.port = '22'
env.local_dir = './_book/'
env.remote_dir = '/home/apps/docs/'

@task
def clean(migrate=None):
    local('find . -name "*.pyc" | xargs rm -rf')
    local('find . -name "*.bak" | xargs rm -rf')
    local('find . -name "*.log" | xargs rm -rf')
    local('rm -rf assets/static/*')


@task
def md():
    su = open('SUMMARY.md').read()
    tx = re.findall(r'\[(.*?)\]', su)
    nu = 0

    for x in re.findall(r'\((.*?)\)', su):
        if not os.path.exists(x):
            pass
        else:
            print len(open(x).read())
        # t = '''%s\n====''' % tx[nu]
        # print 'echo %s > %s' % (t,x)
    nu += 1


def apache2conf(prefix='docs'):
    conf = '''
<VirtualHost 61.135.149.99:80>
    ServerName %s.mi-tang.com
    Include /etc/apache2/vhosts.d/default_vhost.include
    DocumentRoot "/home/www/mi-tang.com/%s"
    <Directory "/home/www/mi-tang.com/%s">
        Options -Indexes FollowSymLinks
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
    <IfModule mpm_peruser_module>
        ServerEnvironment apache apache
    </IfModule>
    CustomLog /home/logs/access.%s.mi-tang.com.log combined
</VirtualHost>''' % (prefix, prefix, prefix, prefix)
    
    return open('default.conf', 'w').write(conf)

@task
def setup():
    apache2conf('docs')
    run('mkdir -p %s' % env.remote_dir)
    put('default.conf','/etc/apache2/vhosts.d/010-docs.mi-tang.conf')
    run('/etc/init.d/apache2 restart')

@task
def serve():
    local('gitbook serve .')
    project.rsync_project(
        remote_dir=env.remote_dir,
        local_dir=env.local_dir,
        delete=True
    )

@task
def sync():
    local('gitbook build .')
    project.rsync_project(
        remote_dir=env.remote_dir,
        local_dir=env.local_dir,
        delete=True
    )
