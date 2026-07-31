%define upstream_name    GPS-Lowrance
%define upstream_version 0.31
Name:		perl-%{upstream_name}
Version:	0.31
Release:	2

Summary:	Convert between mercator meters and degrees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/GPS-Lowrance
Source0:	https://cpan.metacpan.org/authors/id/R/RR/RRWO/GPS-Lowrance-0.31.tar.gz

BuildRequires:	make
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
%setup -q -n GPS-Lowrance-0.31

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
#make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

