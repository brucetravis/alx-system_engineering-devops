# Puppet manifest to adjust OS configuration for holberton user

# Adjust limits for the holberton user
file { '/etc/security/limits.conf':
    ensure  => present,
    content => "holberton hard nofile 1024\nholberton soft nofile 1024\n",
}

# Apply changes to the holberton user's session
exec { 'reload_pam_limits':
    command     => 'pam_limits.so',
    path        => '/bin:/sbin:/usr/bin:/usr/sbin',
    refreshonly => true,
    subscribe   => File['/etc/security/limits.conf'],
}

# Notify login changes
notify { 'OS configuration adjusted for holberton user':
    message => 'OS configuration adjusted for holberton user',
    require => Exec['reload_pam_limits'],
}
