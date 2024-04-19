# This Puppet manifest installs Flask package using pip3
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command   => '/usr/bin/pip3 install Flask==2.1.0',
  path      => ['/usr/bin'],
  creates   => '/usr/local/lib/python3.8/dist-packages/flask/__init__.py',
  unless    => 'test -f /usr/local/lib/python3.8/dist-packages/flask/__init__.py && /usr/bin/flask --version | grep -q "Flask 2.1.0"',
  timeout   => 300,  # Set a timeout for the execution
  logoutput => true,  # Log the output of the execution
}
