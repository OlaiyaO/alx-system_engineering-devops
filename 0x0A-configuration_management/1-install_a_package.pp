# This Puppet manifest installs Flask package using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
