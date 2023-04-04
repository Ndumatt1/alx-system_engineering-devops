# This script confiures nginx using puppet
exec { 'install_nginx':
  command  => 'apt-get update && apt-get install -y nginx',
  provider => shell,
}

exec { 'add_custom_header':
  command  => "sed -i '/http {/a add_header X-Served-By ${facts['hostname']};' /etc/nginx/nginx.conf",
  onlyif   => "grep -q 'add_header X-Served-By ${facts['hostname']};' /etc/nginx/nginx.conf",
  provider => shell,
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
  provider    => shell,
  subscribe   => Exec['add_custom_header'],
}
