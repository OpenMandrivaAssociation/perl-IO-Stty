%define	module	IO-Stty
%define	name	perl-%{module}
%define	module	IO-Stty
%define	version	02
%define	release	%mkrel 9

Summary:	IO-Stty perl module
Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
License: 	GPL
Group: 		Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{module}-.%{version}.tar.bz2
Url:		http://www.cpan.org
Buildrequires:	perl-devel
Patch0:		%{name}-paths.patch
Requires: 	perl, perl-base >= 5.8.6
Buildarch:	noarch

%description
IO-Stty is a module for setting terminal parameters.

%prep
%setup -q -n %{module}-.%{version}

%patch -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README stty.txt
%{perl_vendorlib}/IO/*


