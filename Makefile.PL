use inc::Module::Install;

name 'App-meta2spec';
all_from 'bin/meta2spec';

requires 'YAML';
requires 'POSIX';

install_script 'bin/meta2spec';
license 'perl';

WriteAll;
