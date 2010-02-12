%define	upstream_name	 IO-Stty
%define	upstream_version .02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	IO-Stty perl module
License: 	GPL
Group: 		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{name}-paths.patch

Buildarch:	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
IO-Stty is a module for setting terminal parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README stty.txt
%{perl_vendorlib}/IO/*
