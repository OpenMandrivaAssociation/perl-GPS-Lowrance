%define upstream_name    GPS-Lowrance
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Convert between mercator meters and degrees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module provides a variety of low- and high-level methods for
communicating with Lowrance and Eagle GPS receivers which support the LSI
100 protocol. It also provides some utility functions for converting data.

This module is a work in progress.

Methods
    * connect

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 654192
- rebuild for updated spec-helper

* Sun May 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 381691
- import perl-GPS-Lowrance


* Sun May 31 2009 cpan2dist 0.31-1mdv
- initial mdv release, generated with cpan2dist

