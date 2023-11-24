# install_flask.pp

package { 'python3-pip':
  ensure => present,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'upgrade_werkzeug':
  command => '/usr/bin/pip3 install --upgrade Werkzeug',
  require => Package['Flask'],
}
