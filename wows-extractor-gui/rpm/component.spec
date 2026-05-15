%global debug_package %{nil}

%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        World of Warships graphical resource extractor and model viewer
License:        GPL-3.0
URL:            https://github.com/wows-tools/wows-extractor-gui
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquick3d-devel
BuildRequires:  zlib-devel
BuildRequires:  pcre2-devel
BuildRequires:  meshoptimizer-devel
BuildRequires:  tinygltf-devel
BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  make

%description
wows-extractor-gui is a Qt6 graphical tool for browsing World of Warships
resource packages, extracting files, and previewing ship 3D geometry in
glTF/GLB format. Requires OpenGL 3.3 Core support and a local World of
Warships installation.

%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%files
%{_bindir}/wows-extractor

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package
