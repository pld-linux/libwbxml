Summary:	WBXML2 Library
Summary(pl):	Biblioteka WBXML2
Name:		wbxml2
Version:	0.9.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/wbxmllib/%{name}-%{version}-src.tar.gz
# Source0-md5:	3f9b5bf104ec523b8eebe69f93919ded
Patch0:		http://www.multisync.org/files/%{name}-0.9.0.patch
URL:		http://libwbxml.aymerick.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The WBXML2 format is a binary representation of XML, defined by the
Wap Forum, and used to reduce bandwidth in mobile communications.

%description -l pl
Format WBXML2 jest binarn± reprezentacj± XML, zdefiniowan± przez Wap
Forum, maj±c± na celu zmniejszenie ruchu w komunikacji przez
urz±dzenia przeno¶ne.

%package devel
Summary:	Header files for WBXML2 library
Summary(pl):	Pliki nag³ówkowe biblioteki WBXML2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for WBXML2 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki WBXML2.

%package static
Summary:	Static WBXML2 library
Summary(pl):	Statyczna biblioteka WBXML2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WBXML2 library.

%description static -l pl
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
