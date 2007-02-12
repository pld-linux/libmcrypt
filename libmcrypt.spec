#
%bcond_with	modules	# build algos and modes as loadable modules
#			  (warning: ltdl has memory leaks, so it's insecure
#			   in persistent environment, e.g. apache+php)
#
Summary:	Encryption/decryption library
Summary(pl.UTF-8):   Biblioteka z funkcjami szyfrującymi oraz deszyfrującymi
Name:		libmcrypt
Version:	2.5.7
Release:	2
License:	LGPL
Vendor:		Nikos Mavroyanopoulos <nmav@hellug.gr>
Group:		Libraries
Source0:	http://dl.sourceforge.net/mcrypt/%{name}-%{version}.tar.gz
# Source0-md5:	b1be163143f8e8ed0474beeb642b3bad
Patch0:		%{name}-am18.patch
URL:		http://mcrypt.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_modules:BuildRequires:	libltdl-devel}
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

%description -l pl.UTF-8
Zamiennik dla starej uniksowej funkcji crypt(). Mcrypt używa
następujących algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i
GOST. Uniksowy algorytm crypt także jest obsługiwany by zachować
kompatybilność z crypt(1).

%package devel
Summary:	Header files and development documentation for libmcrypt
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do libmcrypt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_modules:Requires:	libltdl-devel}

%description devel
Header files and development documentation for libmcrypt.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libmcrypt.

%package static
Summary:	Encryption/decryption static library
Summary(pl.UTF-8):   Statyczna biblioteka z funkcjami szyfrującymi oraz deszyfrującymi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Encryption/decryption static library.

%description static -l pl.UTF-8
Statyczna biblioteka z funkcjami szyfrującymi oraz deszyfrującymi.

%prep
%setup -q
%patch0 -p1

# only invalid libtool.m4 inclusion
rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd libltdl
%{__aclocal}
%{__autoconf}
# don't use -f here
automake -a -c --foreign
cd ..
%configure \
	--enable-static \
	--disable-libltdl \
	%{?with_modules:--enable-dynamic-loading}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS KNOWN-BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%if %{with modules}
%dir %{_libdir}/libmcrypt
%attr(755,root,root) %{_libdir}/libmcrypt/*.so
%{_libdir}/libmcrypt/*.la
%endif

%files devel
%defattr(644,root,root,755)
%doc ChangeLog doc/README.*
%attr(755,root,root) %{_bindir}/libmcrypt-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
