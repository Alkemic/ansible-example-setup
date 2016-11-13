#!/bin/bash

cat >/etc/apt/sources.list.d/ansible-ansible-jessie.list <<EOL
deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main
deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main
EOL

apt-get update
apt-get install -y --force-yes ansible
