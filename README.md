[![Build Packages Repositories](https://github.com/wows-tools/wows-pkg/actions/workflows/repos.yml/badge.svg)](https://github.com/wows-tools/wows-pkg/actions/workflows/repos.yml)
[![Check CVEs on NVD](https://github.com/wows-tools/wows-pkg/actions/workflows/vulncheck.yml/badge.svg)](https://github.com/wows-tools/wows-pkg/actions/workflows/vulncheck.yml)


# wows-pkg

Collection of `.deb`/`.rpm` packages for World of Warships tools.

The repositories are available at: https://wows-tools.github.io/wows-pkg/

## Packaged Projects

### My projects

| Package | Description |
|---------|-------------|
| [wows-depack](https://github.com/wows-tools/wows-depack) | CLI and library for unpacking World of Warships resource archives |
| [wows-extractor-gui](https://github.com/wows-tools/wows-extractor-gui) | Graphical resource extractor and 3D model viewer |
| [wows-fuse](https://github.com/wows-tools/wows-fuse) | FUSE filesystem for mounting World of Warships resource packages |
| [wows-model-exporter](https://github.com/wows-tools/wows-model-exporter) | 3D model export tools and geometry parsing library |
| [wows-splash](https://github.com/wows-tools/wows-splash) | CLI and library for parsing World of Warships splash files |

### Third-party projects

| Package | Description | Original Author |
|---------|-------------|-----------------|
| [wows-monitor](https://wows-monitor.com/) | Matchmaking monitor for World of Warships | [wows-monitor.com](https://wows-monitor.com/) |
| [wows-toolkit](https://github.com/landaire/wows-toolkit) | Swiss army knife for WoWS: replay browser, file extractor, armor viewer, and unpack CLI | [landaire](https://github.com/landaire) |

## Ubuntu/Debian

If you are using `Ubuntu`/`Debian`, here how to install the repository:

```shell
# If you are not root
export SUDO=sudo

# Get your OS version
. /etc/os-release
# Get the architecture
ARCH=$(dpkg --print-architecture)

# Add the GPG key
${SUDO} install -dm755 /etc/apt/keyrings
wget -qO - https://wows-tools.github.io/wows-pkg/GPG-KEY.pub | \
    ${SUDO} tee /etc/apt/keyrings/wows-pkg.asc >/dev/null

# Add the repository
cat << EOF | ${SUDO} tee /etc/apt/sources.list.d/wows-pkg.sources
Types: deb
URIs: https://wows-tools.github.io/wows-pkg/deb.${VERSION_CODENAME}.${ARCH}/
Suites: ${VERSION_CODENAME}
Components: main
Architectures: ${ARCH}
Signed-By: /etc/apt/keyrings/wows-pkg.asc
EOF

# update
${SUDO} apt update
```

## RHEL/Rocky/Fedora

If you are using `RHEL`/`Rocky`/`Fedora`, here how to install the repository:

```shell
# If you are not root
export SUDO=sudo

# Get your OS version
. /etc/os-release

# Determine distro prefix (el for RHEL/Rocky, fc for Fedora)
if [[ "$ID" == "fedora" ]]; then
    DISTRO_PREFIX="fc"
else
    DISTRO_PREFIX="el"
fi

# Create the repository file
cat << EOF | ${SUDO} tee -a /etc/dnf/dnf.conf

[wows-pkg]
name=wows-pkg
baseurl=https://wows-tools.github.io/wows-pkg/rpm.${DISTRO_PREFIX}\$releasever.\$basearch/\$releasever/\$basearch/
enabled=1
gpgcheck=1
gpgkey=https://wows-tools.github.io/wows-pkg/GPG-KEY.pub
EOF
```

## Building

Check the [pakste documentation](https://kakwa.github.io/pakste/).
