# Puppet manifest to optimize Nginx configuration

# Define a class to manage Nginx configuration
class nginx_config {

    # Define the main Nginx configuration file
    file { '/etc/nginx/nginx.conf':
        ensure  => file,
        content => template('nginx/nginx.conf.erb'),
        notify  => Service['nginx'],
    }

    # Define the Nginx service
    service { 'nginx':
        ensure  => running,
        enable  => true,
        require => File['/etc/nginx/nginx.conf'],
    }
}

# Apply the nginx_config class
include nginx_confign
