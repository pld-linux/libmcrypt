Summary:	encryption/decryption library
Summary(pl):	biblioteka z funkcjami szyfruj±cymi oraz deszyfruj±cymi
Name:		libmcrypt
Version:	2.4.16
Release:	1
License:	LGPL
Vendor:		Nikos Mavroyanopoulos <nmav@hellug.gr>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://mcrypt.hellug.gr/pub/mcrypt/libmcrypt/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A replacement for the old unix crypt(1) command. Mcrypt uses the
following encryption (block) algorithms: BLOWFISH, DES, TripleDES,
3-WAY, SAFER-SK64, SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH,
RC6, IDEA and GOST. The unix crypt algorithm is also included, to
allow compability with the crypt(1) command.

CBC, ECB, OFB and CFB modes of encryption are supported. A library
which allows access to the above algorithms and modes is included.

%description -l pl
Zamiennik dla starej unixowej funkcji crypt(). Mcrypt u¿ywa
nastêpuj±cych algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i
GOST. Unixowy algorytm crypt tak¿e jest obs³ugiwany by zachowaæ
kompatybilno¶æ z crypt(1).

%package devel
Summary:	Header files and development documentation for libmcrypt
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libmcrypt
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libmcrypt.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do libmcrypt.

%package static
Summary:	Encryption/decryption static library
Summary(pl):	Statyczna biblioteka z funkcjami szyfruj±cymi oraz deszyfruj±cymi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Encryption/decryption static library.

%description -l pl static
Statyczna biblioteka z funkcjami szyfruj±cymi oraz deszyfruj±cymi.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
(cd libltdl
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c)
%configure \
	--enable-static \
	--disable-libltdl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

gzip -9nf ChangeLog doc/README.*

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/libmcrypt
%attr(755,root,root) %{_libdir}/libmcrypt/*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/libmcrypt-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/libmcrypt/*.la
%{_mandir}/man3/*
%{_includedir}/*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/libmcrypt/*.a
