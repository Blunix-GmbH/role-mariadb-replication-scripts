import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_root_password(host):
    assert host.run("mysql -uroot -pmolecule").rc == 0


def test_configuration_template(host):
    assert host.file("/etc/mysql/mariadb.conf.d/98-ansible.cnf").contains('bind-address = 127.0.0.1')
    assert host.file("/etc/mysql/mariadb.conf.d/99-custom.cnf").contains('key_buffer_size = 16M')


def test_service_running(host):
    assert host.service('mysqld').is_running
