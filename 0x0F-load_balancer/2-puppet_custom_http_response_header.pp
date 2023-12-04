cript to configure Nginx with a custom HTTP header

class custom_http_response_header {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
                  listen 80 default_server;
                  listen [::]:80 default_server;

                  server_name _;

                  location / {
                      add_header X-Served-By $hostname;
                      proxy_pass http://backend;
                  }

                  location /status {
                      access_log off;
                      allow 127.0.0.1;
                      deny all;
                      stub_status;
                  }
              }
    ",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }
}

include custom_http_response_header
