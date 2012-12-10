%define name cwirc
%define version 2.0.0
%define release %mkrel 5

Summary: X-Chat Morse plugin
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://webperso.easyconnect.fr/om.the/web/cwirc/download/
Source: http://webperso.easyconnect.fr/om.the/web/cwirc/download/%{name}-%{version}.tar.bz2
License: GPL
Group: Networking/IRC
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: gtk2-devel
Requires: xchat >= 2.0.2

%description
X-Chat plugin for sending and receiving raw morse code over IRC.

%prep
%setup -q

%build
make TARGET_OS=LINUX PLUGIN_INSTALL_DIRECTORY=dummy			\
	FRONTEND_INSTALL_DIRECTORY=dummy				\
	CWIRC_EXTENSIONS_DIRECTORY=%{_libdir}/cwirc/extensions

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/xchat/plugins
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/cwirc/extensions
cp cwirc.so $RPM_BUILD_ROOT/%{_libdir}/xchat/plugins
cp cwirc_frontend $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changelog COPYING schematics/cw_oscillator.jpg schematics/rs232_key_connection.jpg
%{_libdir}/xchat/plugins/cwirc.so
%{_bindir}/cwirc_frontend
%{_libdir}/cwirc/extensions



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdv2011.0
+ Revision: 617488
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-4mdv2010.0
+ Revision: 426166
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-3mdv2009.0
+ Revision: 243845
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.0.0-1mdv2008.1
+ Revision: 123623
- kill re-definition of %%buildroot on Pixel's request
- import cwirc


* Tue May 23 2006 Lenny Cartier <lenny@mandriva.com> 2.0.0-1mdk
- 2.0.0

* Thu Oct 20 2005 Lenny Cartier <lenny@mandriva.com> 1.8.8-2mdk
- rebuild

* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.8.8-1mdk
- 1.8.8

* Mon Jul 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.8.7-1mdk
- 1.8.7

* Wed Jan 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.7.4-1mdk
- from P.P. Coupard <pcoupard@easyconnect.fr> :
	- First draft of the spec file
