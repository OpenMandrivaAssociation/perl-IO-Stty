%define	upstream_name	 IO-Stty
%define	upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Epoch:      1

Summary:	IO-Stty perl module
License: 	GPL
Group: 		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch:	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
IO-Stty is a module for setting terminal parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_bindir}/stty.pl
%{_mandir}/*
%{perl_vendorlib}/IO/*
