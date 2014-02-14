Summary:	X-Chat Morse plugin
Name:		cwirc
Version:	2.0.0
Release:	6
License:	GPLv2+
Group:		Networking/IRC
Url:		http://webperso.easyconnect.fr/om.the/web/cwirc/download/
Source0:	http://webperso.easyconnect.fr/om.the/web/cwirc/download/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	xchat >= 2.0.2

%description
X-Chat plugin for sending and receiving raw morse code over IRC.

%files
%doc README Changelog COPYING schematics/cw_oscillator.jpg schematics/rs232_key_connection.jpg
%{_libdir}/xchat/plugins/cwirc.so
%{_bindir}/cwirc_frontend
%{_libdir}/cwirc/extensions

#----------------------------------------------------------------------------

%prep
%setup -q

%build
make \
	CFLAGS="%{optflags} -DLINUX" \
	STRIP=true \
	TARGET_OS=LINUX \
	PLUGIN_INSTALL_DIRECTORY=dummy \
	FRONTEND_INSTALL_DIRECTORY=dummy \
	CWIRC_EXTENSIONS_DIRECTORY=%{_libdir}/cwirc/extensions

%install
mkdir -p %{buildroot}%{_libdir}/xchat/plugins
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/cwirc/extensions
install -m 0755 cwirc.so %{buildroot}%{_libdir}/xchat/plugins
install -m 0755 cwirc_frontend %{buildroot}%{_bindir}/

