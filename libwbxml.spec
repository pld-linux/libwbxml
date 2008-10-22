# TODO:
# - kill unecessary -lnsl etc.
# - lib is linked with -lexpat, but .pc specifies libxml2
# - remove libxml junk from wbxml_tree.h - it breaks php-wbxml.spec
# - maybe add datetime.patch from synce repository
# - add changeset 59 (fix for segfault)
# - namespace.patch from synce trunk contains some improvements
#
Summary:	WBXML2 Library
Summary(pl.UTF-8):	Biblioteka WBXML2
Name:		wbxml2
Version:	0.9.2
Release:	3.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/wbxmllib/%{name}-%{version}.tar.gz
# Source0-md5:	67a48fd9b69db8818a4dca5375c7993a
Patch0:		%{name}-r34.patch
Patch1:		%{name}-r35.patch
Patch2:		%{name}-r39.patch
Patch3:		%{name}-r41.patch
Patch4:		%{name}-r42.patch
Patch5:		%{name}-r43.patch
Patch6:		%{name}-r44.patch
Patch7:		%{name}-prepare-r48.patch
Patch8:		%{name}-r48.patch
Patch9:		%{name}-r49.patch
Patch10:	%{name}-r52.patch
Patch11:	%{name}-r57.patch
Patch12:	%{name}-r58.patch
#Patch13:	http://synce.svn.sourceforge.net/viewvc/synce/trunk/patches/wbxml-svn-r53-namespace.patch?revision=2914
Patch13:	%{name}-namespace.patch
URL:		http://libwbxml.aymerick.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Obsoletes:	libwbxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The WBXML2 format is a binary representation of XML, defined by the
Wap Forum, and used to reduce bandwidth in mobile communications.

%description -l pl.UTF-8
Format WBXML2 jest binarną reprezentacją XML, zdefiniowaną przez Wap
Forum, mającą na celu zmniejszenie ruchu w komunikacji przez
urządzenia przenośne.

%package devel
Summary:	Header files for WBXML2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WBXML2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libwbxml2-devel

%description devel
Header files for WBXML2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WBXML2.

%package static
Summary:	Static WBXML2 library
Summary(pl.UTF-8):	Statyczna biblioteka WBXML2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WBXML2 library.

%description static -l pl.UTF-8
Statyczna biblioteka WBXML2.

%prep
%setup -q
%patch0 -p3
%patch1 -p3
%patch2 -p3
%patch3 -p3
%patch4 -p3
%patch5 -p3
%patch6 -p3
%patch7 -p0
%patch8 -p3
%patch9 -p3
%patch10 -p3
%patch11 -p3
%patch12 -p3
%patch13 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/wbxml2xml
%attr(755,root,root) %{_bindir}/xml2wbxml
%attr(755,root,root) %{_libdir}/libwbxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwbxml2.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwbxml2.so
%{_libdir}/libwbxml2.la
%{_includedir}/wbxml*.h
%{_pkgconfigdir}/libwbxml2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwbxml2.a
