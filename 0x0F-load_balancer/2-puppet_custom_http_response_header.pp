# Puppet manifest for customizing a 404-error_page

# Updating Packages before performing installations
package { 'nginx':
  ensure => 'latest',
  require => Exec['apt-update'],
}

exec { 'apt-update':
  command => 'apt-get update',
  path    => '/usr/bin',
  refreshonly => true,
}

# Creating an index.html page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Implementing a "moved permanently redirection" (301)
file_line { 'nginx_redirect_rule':
  path    => '/etc/nginx/sites-enabled/default',
  line    => '    rewrite ^/redirect_me https://github.com/OlaiyaO permanent;',
  require => Package['nginx'],
}

# Creating a custom 404 error page
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

file_line { 'nginx_404_config':
  path    => '/etc/nginx/sites-enabled/default',
  line    => "    error_page 404 /404.html;\n    location = /404.html {\n        root /var/www/html;\n        internal;\n    }",
  require => Package['nginx'],
}

# Adding an HTTP response header
file_line { 'nginx_header_config':
  path    => '/etc/nginx/sites-enabled/default',
  line    => "    add_header X-Served-By $hostname;",
  require => Package['nginx'],
}

# Checking configurations for syntax errors
exec { 'nginx-syntax-check':
  command => 'nginx -t',
  path    => '/usr/sbin',
  notify  => Service['nginx'],
}

# Restarting nginx to apply changes
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
  subscribe => Exec['nginx-syntax-check'],
}
