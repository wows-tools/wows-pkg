%global debug_package %{nil}

%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        Matchmaking monitor for World of Warships
License:        unknown
URL:            https://wows-monitor.com/
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  make

%description
wows-monitor is a real-time companion application for World of Warships
that displays current player statistics for allies and enemies during
an active match.

Note: the build downloads npm packages and the Electron runtime from the
internet; an internet-connected build environment is required.

%prep
%setup -q
patch -p1 < debian/patches/Avoid-building-unnecessary-packages.patch

%build
npm install
npm run electron:package:l

%install
install -d %{buildroot}/%{_datadir}/wows-monitor
cp -dr --no-preserve=ownership release/build/linux-unpacked/. %{buildroot}/%{_datadir}/wows-monitor/
install -d %{buildroot}/%{_datadir}/applications
install -Dm644 debian/wows-monitor.desktop \
    %{buildroot}/%{_datadir}/applications/wows-monitor.desktop
install -d %{buildroot}/%{_bindir}
ln -s %{_datadir}/wows-monitor/wows-monitor %{buildroot}/%{_bindir}/wows-monitor

%files
%{_datadir}/wows-monitor/
%{_datadir}/applications/wows-monitor.desktop
%{_bindir}/wows-monitor

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package
