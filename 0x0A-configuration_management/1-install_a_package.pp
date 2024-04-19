#!/usr/bin/pup
# This Puppet manifest installs Flask package using pip

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
