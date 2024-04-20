#!/usr/bin/env bash
# Making some changes to our configuration file using puppet

file { '/etc/ssh/ssh_config':
	ensure => present,

content =>"

	#configuring SSH client
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	"

}
