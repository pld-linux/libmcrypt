Summary:	encryption/decryption library
Summary(pl):	biblioteka z funkcjami szyfrującymi oraz deszyfrującymi
Name:		libmcrypt
Version:	2.2.1
Release:	1
Vendor:		Nikos Mavroyanopoulos <nmav@hellug.gr>
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://argeas.cs-net.gr/pub/unix/mcrypt/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A replacement for the old unix crypt(1) command. Mcrypt uses the following
encryption (block) algorithms: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH, RC6, IDEA and GOST. The
unix crypt algorithm is also included, to allow compability with the
crypt(1) command.

CBC, ECB, OFB and CFB modes of encryption are supported. A library which
allows access to the above algorithms and modes is included.

%description -l pl
Zamiennik dla starej unixowej funkcji crypt(). Mcrypt używa następujących
algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64, SAFER-SK128, CAST-128,
RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i GOST. Unixowy algorytm crypt także
jest obsługiwany by zachować kompatybilność z crypt(1).

%package devel
Summary:	Header files and development documentation for libmcrypt
Summary(pl):	Pliki nagłówkowe i dokumentacja do libmcrypt
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libmcrypt.

%description -l pl devel
Pliki nagłówkowe i dokumentacja do libmcrypt.

%package static
Summary:	Encryption/decryption static library
Summary(pl):	Statyczna biblioteka z funkcjami szyfrującymi oraz deszyfrującymi
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Encryption/decryption static library.

%description -l pl static
Statyczna biblioteka z funkcjami szyfrującymi oraz deszyfrującymi.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR="$RPM_BUILD_ROOT" install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	ChangeLog doc/{README.key,README.lib,README.mcrypt}

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {ChangeLog,doc/{README.key,README.lib,README.mcrypt}}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
