%define	modname	IO-Stty
%define	modver	0.08

Summary:	IO-Stty perl module
Name:		perl-%{modname}
Epoch:		1
Version:	%{modver}
Release:	3
License:	GPLv2
Group:		Development/Perl
Url:		https://github.com/cpan-authors/IO-Stty
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Stty-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build) => 0.35

%description
IO-Stty is a module for setting terminal parameters.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
make test

%install
%make_install

%files
%doc README
%{_bindir}/stty.pl
%{perl_vendorlib}/IO/*
%doc %{_mandir}/man3/*

