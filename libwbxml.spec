# TODO:
# - maybe add datetime.patch from synce repository
# - namespace.patch from synce trunk contains some improvements
# - build dynamic documentation                  OFF
#
Summary:	The WBXML Library
Summary(pl.UTF-8):	Biblioteka WBXML
Name:		libwbxml
Version:	0.10.8
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwbxml/%{name}-%{version}.tar.bz2
# Source0-md5:	7b51c425fc2ff9f502cd9b1e291b1955
Patch0:		wbxml2-r59.patch
URL:		http://libwbxml.opensync.org/
BuildRequires:	cmake
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.577
BuildConflicts:	wbxml2
Obsoletes:	libwbxml2
Obsoletes:	wbxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The WBXML Library (libwbxml) contains a library and its associated
tools to parse, encode and handle WBXML documents. The WBXML format is
a binary representation of XML, defined by the Wap Forum, and used to
reduce bandwidth in mobile communications.

%description -l pl.UTF-8
Format WBXML jest binarną reprezentacją XML, zdefiniowaną przez Wap
Forum, mającą na celu zmniejszenie ruchu w komunikacji przez
urządzenia przenośne.

%package devel
Summary:	Header files for WBXML library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WBXML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libwbxml2-devel
Obsoletes:	wbxml2-devel
Obsoletes:	wbxml2-static

%description devel
Header files for WBXML library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WBXML.

%prep
%setup -q
%patch0 -p3

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_VERBOSE_MAKEFILE=ON \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains just license information, not LGPL text itself
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO References
%attr(755,root,root) %{_bindir}/wbxml2xml
%attr(755,root,root) %{_bindir}/xml2wbxml
%attr(755,root,root) %{_libdir}/libwbxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwbxml2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwbxml2.so
%{_includedir}/wbxml*.h
%{_pkgconfigdir}/libwbxml2.pc
