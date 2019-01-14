#!/bin/bash
(ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ./deploy/deploy.yml -u ubuntu -i ./hosts --private-key=\
/home/jenkins/.ssh/id_rsa)