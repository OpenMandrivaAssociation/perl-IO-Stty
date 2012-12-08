%define	upstream_name	 IO-Stty
%define	upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    7
Epoch:		1

Summary:	IO-Stty perl module
License: 	GPL
Group: 		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build) => 0.35
BuildArch:	noarch

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
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README
%{_bindir}/stty.pl
%{_mandir}/man3/*
%{perl_vendorlib}/IO/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.30.0-6mdv2012.0
+ Revision: 765375
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.30.0-4
+ Revision: 676891
- fix deps
- rebuild
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1:0.30.0-2mdv2011.0
+ Revision: 564736
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.30.0-1mdv2011.0
+ Revision: 552367
- update to 0.03

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.20.0-1mdv2010.1
+ Revision: 504893
- bump epoch
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 02-11mdv2010.0
+ Revision: 426512
- rebuild

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 02-10mdv2009.1
+ Revision: 360223
- fix patch num

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 02-10mdv2009.0
+ Revision: 223800
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 02-9mdv2008.1
+ Revision: 180412
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 02-8mdv2008.0
+ Revision: 23390
- rebuild


* Tue Feb 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 02-7mdk
- rebuild

* Sun Aug 17 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 02-6mdk
- rebuild for new perl
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- drop $RPM_OPT_FLAGS, noarch..

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 02-5mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 02-4mdk
- buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 02-3mdk
- rebuild

* Wed Jul 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 02-2mdk
- rebuild with new perl

* Mon Sep 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 02-1mdk
- added by Max Heijndijk <cchq@wanadoo.nl> :
	- Initial wrap

