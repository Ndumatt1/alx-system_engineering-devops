# Configures server to use private key ~/.ssh/school
file { '/etc/ssh/ssh_config':
    ensure  => file,
	mode    => '0600',
	content => "
Host 54.144.156.217
	    PasswordAuthentication no
		IdentityFile ~/.ssh/school
"
}
