%define	modname	IO-Stty
%define	modver	0.03

Summary:	IO-Stty perl module
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build) => 0.35

%description
IO-Stty is a module for setting terminal parameters.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README
%{_bindir}/stty.pl
%{perl_vendorlib}/IO/*
%{_mandir}/man3/*

