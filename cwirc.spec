%define name cwirc
%define version 2.0.0
%define release %mkrel 3

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

