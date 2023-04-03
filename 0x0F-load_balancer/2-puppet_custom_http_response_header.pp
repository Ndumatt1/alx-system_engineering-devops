# This script confiures nginx using puppet

exec { 'install':
  command  => 'sudo apt-get install -y nginx',
  provider => shell,
}

exec { 'sed -i "/http {/a \
  add_header X-Served-By $hostname;" /etc/nginx/nginx.conf':
  provider => shell,
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
