cription: Puppet manifest to adjust user limits for the holberton user

# Define a custom limit for the holberton user
user { 'holberton':
  limitssh   => '5000:5000', # Set the limit as needed
  managehome => true,
}

# Apply the changes to the user limits
exec { 'apply_user_limits':
  command     => 'ulimit -n 5000', # Set the limit as needed
  user        => 'holberton',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  subscribe   => User['holberton'],
  refreshonly => true,
}

# Restart the ssh service to apply the changes
service { 'ssh':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
  subscribe  => Exec['apply_user_limits'],
}
