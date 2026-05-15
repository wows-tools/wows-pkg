%global debug_package %{nil}

%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        World of Warships tools suite
License:        MIT
URL:            https://github.com/landaire/wows-toolkit
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
# Rust 1.92+ required; install via rustup if the system toolchain is too old.
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  make

%description
wows-toolkit is a Swiss army knife for World of Warships, providing a GUI
application and CLI tools for browsing replays, extracting game files, viewing
armor models, and analysing replay data.

Binaries provided:
  wows_toolkit  - GUI application (requires Vulkan/OpenGL 3.3+)
  wowsunpack    - CLI tool for unpacking IDX/PKG game asset archives
  replayshark   - CLI tool for analysing replay files

%prep
%setup -q

%build
# .cargo/config.toml with vendored-sources is embedded in the source tarball.
cargo build --release --offline

%install
install -Dm755 target/release/wows_toolkit  %{buildroot}/%{_bindir}/wows_toolkit
install -Dm755 target/release/wowsunpack    %{buildroot}/%{_bindir}/wowsunpack
install -Dm755 target/release/replayshark   %{buildroot}/%{_bindir}/replayshark
install -Dm644 assets/wows-toolkit.desktop  %{buildroot}/%{_datadir}/applications/wows-toolkit.desktop
install -Dm644 assets/wows_toolkit.png      %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/io.github.landaire.WoWsToolkit.png

%files
%{_bindir}/wows_toolkit
%{_bindir}/wowsunpack
%{_bindir}/replayshark
%{_datadir}/applications/wows-toolkit.desktop
%{_datadir}/icons/hicolor/256x256/apps/io.github.landaire.WoWsToolkit.png

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package
