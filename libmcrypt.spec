Summary:	encryption/decryption library
Summary(pl):	biblioteka z funkcjami szyfruj±cymi oraz deszyfruj±cymi
Name:		libmcrypt
Version:	2.2.1
Release:	1
Vendor:		Nikos Mavroyanopoulos <nmav@hellug.gr>
Copyright:	LGPL
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Source:		ftp://argeas.cs-net.gr/pub/unix/mcrypt/%{name}-%{version}.tar.gz
Prereq:		/sbin/ldconfig
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
Zamiennik dla starej unixowej funkcji crypt(). Mcrypt u¿ywa nastêpuj±cych
algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64, SAFER-SK128, CAST-128,
RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i GOST. Unixowy algorytm crypt tak¿e
jest obs³ugiwany by zachowaæ kompatybilno¶æ z crypt(1).

%package static
Summary:        encryption/decryption static library
Summary(pl):    statyczna biblioteka z funkcjami szyfruj±cymi oraz deszyfruj±cymi
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name} = %{version}

%description static
encryption/decryption static library

%description static -l pl
statyczna biblioteka z funkcjami szyfruj±cymi oraz deszyfruj±cymi

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR="$RPM_BUILD_ROOT" install

strip		$RPM_BUILD_ROOT%{_libdir}/*.so
gzip -9nf	$RPM_BUILD_ROOT%{_mandir}/man3/* \
		ChangeLog doc/{README.key,README.lib,README.mcrypt}

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,doc/{README.key,README.lib,README.mcrypt}}.gz
%attr(755,root,root) %{_libdir}/lib*.s*
%{_mandir}/man3/*
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
