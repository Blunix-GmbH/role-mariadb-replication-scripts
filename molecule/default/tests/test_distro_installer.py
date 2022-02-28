import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_install(host):
    assert host.package("mariadb-server-10.3").is_installed


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:3306").is_listening
