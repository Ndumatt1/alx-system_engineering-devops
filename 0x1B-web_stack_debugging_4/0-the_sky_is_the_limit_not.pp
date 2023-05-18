# update the ulimit of the nginx process
exec { 'increase-ulimit':
  command => 'sed -i "s/15/20000/" /etc/default/nginx',
  path    => ['/usr/local/bin/', '/bin/'],
}
exec { 'restart':
  command => 'nginx restart',
  path    => ['/etc/init.d/']
}
