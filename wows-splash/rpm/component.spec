%global debug_package %{nil}

%define soversion 0
%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        World of Warships splash file parser
License:        MIT
URL:            https://github.com/wows-tools/wows-splash
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make

%description
wows-splash is a tool and library for parsing World of Warships .splash files,
which describe ship hitbox geometry.

%package cli
Summary:  Command-line parser for World of Warships splash files
Requires: lib%{name}%{soversion} = %{version}-%{release}

%description cli
Command-line interface for parsing the .splash file format used in
World of Warships, which describes ship hitbox geometry.

%package -n lib%{name}%{soversion}
Summary:  Library for parsing World of Warships splash files

%description -n lib%{name}%{soversion}
Shared library for parsing World of Warships .splash files.
This package contains the runtime library.

%package -n lib%{name}%{soversion}-devel
Summary:  Development files for libwows-splash
Requires: lib%{name}%{soversion} = %{version}-%{release}

%description -n lib%{name}%{soversion}-devel
Development files for the wows-splash library, including header files
needed for developing applications that use wows-splash.


%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{soversion} -p /sbin/ldconfig

%files cli
%{_bindir}/wows-splash-cli

%files -n lib%{name}%{soversion}
%{_libdir}/libwows-splash.so.0*

%files -n lib%{name}%{soversion}-devel
%{_libdir}/libwows-splash.so
%{_includedir}/wows-splash.h

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package
