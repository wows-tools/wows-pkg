%global debug_package %{nil}

%define soversion 0
%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        World of Warships 3D model exporter
License:        MIT
URL:            https://github.com/wows-tools/wows-model-exporter
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  pcre2-devel
BuildRequires:  meshoptimizer-devel
BuildRequires:  tinygltf-devel
BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  make
Requires:       libwows-geometry%{soversion} = %{version}-%{release}

%description
wows-model-exporter parses and exports World of Warships ship geometry to
glTF/GLB format. It provides a library and command-line tools for accessing
ship 3D models.

%package -n libwows-geometry%{soversion}
Summary:  World of Warships geometry parsing library

%description -n libwows-geometry%{soversion}
Shared library for parsing World of Warships ship geometry data and
exporting it to standard 3D formats. This package contains the runtime library.

%package -n libwows-geometry%{soversion}-devel
Summary:  Development files for libwows-geometry
Requires: libwows-geometry%{soversion} = %{version}-%{release}

%description -n libwows-geometry%{soversion}-devel
Development files for the wows-geometry library, including header files
needed for developing applications that use the library.


%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%post -n libwows-geometry%{soversion} -p /sbin/ldconfig
%postun -n libwows-geometry%{soversion} -p /sbin/ldconfig

%files
%{_bindir}/wows-geometry-cli
%{_bindir}/wows-gltf-exporter
%{_bindir}/wows-list-ships

%files -n libwows-geometry%{soversion}
%{_libdir}/libwows-geometry.so.0*

%files -n libwows-geometry%{soversion}-devel
%{_libdir}/libwows-geometry.so
%{_includedir}/wows-geometry.h

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package
