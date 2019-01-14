Ansible with Docker deployment
=======================
This repository is used to deploy web apps which use Docker/Docker Compose using Ansible to an Ubuntu 16.04 server.

The current version generates SSL certificates automatically on the host.

This version also creates automatic database backups daily through cron.


Dependencies
-------------
* Python >=3, >=2.7
* Ansible >=2.5.0

Usage
---------
Install project dependencies::

    $ pip install -r requirements.txt

Update the following variables in ``deploy/group_vars/all.yml``:
* deploy_user
* deploy_group
* code_repository
* app_name
* git_branch
* domain_name
* contact_email

Keys
~~~~~~~~~~
* Add/Change ``connection_key`` to reflect the one you would use to conenct to your remote server.
* Add/Change ``deploy/deploy_key``. Add ``deploy/deploy_key.pub`` to your project's read-only keys.

Hosts
~~~~~~~~~~
* Update the ``hosts`` file to connect to your remote server using a domain name or a public IP address

Run the ansible-playbook through the deploy.sh script::

    $ ./deploy.sh

