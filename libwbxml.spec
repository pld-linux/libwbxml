Summary:	WBXML2 Library
Summary(pl.UTF-8):	Biblioteka WBXML2
Name:		wbxml2
Version:	0.9.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/wbxmllib/%{name}-%{version}.tar.gz
# Source0-md5:	67a48fd9b69db8818a4dca5375c7993a
Patch0:		%{name}-doc.patch
URL:		http://libwbxml.aymerick.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
%patch0 -p1

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
