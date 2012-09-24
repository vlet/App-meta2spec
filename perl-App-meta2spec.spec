Name: perl-App-meta2spec
Version: 0.01
Release: alt1

Summary: extract data from META.yml/MANIFEST and prepare RPM SPEC file
Group: Development/Perl
License: perl

Url: %CPAN App-meta2spec
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(YAML.pm) perl-base perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/meta2spec

%doc Changes README

%changelog
* Mon Sep 24 2012 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt1
- initial build for ALTLinux

