%global debug_package %{nil}

%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        FUSE filesystem for World of Warships resource packages
License:        MIT
URL:            https://github.com/wows-tools/wows-fuse
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  fuse3-devel
BuildRequires:  wows-depack-devel
BuildRequires:  zlib-devel
BuildRequires:  pcre2-devel
BuildRequires:  gcc
BuildRequires:  make
Requires:       fuse3

%description
wows-fuse mounts World of Warships .idx/.pkg resource packages as a virtual
FUSE filesystem, enabling exploration without manual extraction.

%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%files
%{_bindir}/wows-fuse

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package
