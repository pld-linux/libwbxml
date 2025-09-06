# TODO:
# - maybe add datetime.patch from synce repository
# - namespace.patch from synce trunk contains some improvements
# - build dynamic documentation                  OFF
#
Summary:	The WBXML Library
Summary(pl.UTF-8):	Biblioteka WBXML
Name:		libwbxml
Version:	0.11.10
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/libwbxml/libwbxml/archive/libwbxml-%{version}/%{name}-libwbxml-%{version}.tar.gz
# Source0-md5:	c1918b23520f080c5492a496485388e7
URL:		https://github.com/libwbxml/libwbxml
BuildRequires:	cmake >= 3.5
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildConflicts:	wbxml2
Obsoletes:	libwbxml2 < 0.10
Obsoletes:	wbxml2 < 0.10
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
Obsoletes:	libwbxml2-devel < 0.10
Obsoletes:	wbxml2-devel < 0.10
Obsoletes:	wbxml2-static < 0.10

%description devel
Header files for WBXML library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WBXML.

%prep
%setup -q -n %{name}-libwbxml-%{version}

%build
install -d build
cd build
%cmake ..

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
%doc BUGS COPYING ChangeLog README THANKS TODO References
%attr(755,root,root) %{_bindir}/wbxml2xml
%attr(755,root,root) %{_bindir}/xml2wbxml
%attr(755,root,root) %{_libdir}/libwbxml2.so.*.*.*
%ghost %{_libdir}/libwbxml2.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libwbxml2.so
%{_includedir}/libwbxml-1.1
%{_pkgconfigdir}/libwbxml2.pc
%{_libdir}/cmake/libwbxml2
