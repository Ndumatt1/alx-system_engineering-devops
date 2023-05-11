# puppet script to replace a typo on /var/www/hmtl/wp-settings.php
exec { 'replace':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin']
}
