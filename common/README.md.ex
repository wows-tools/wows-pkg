[![Build Packages Repositories](https://github.com/@ORG@/@REPO@/actions/workflows/repos.yml/badge.svg)](https://github.com/@ORG@/@REPO@/actions/workflows/repos.yml)
[![CVEs/NVD Check](https://github.com/@ORG@/@REPO@/actions/workflows/vulncheck.yml/badge.svg)](https://github.com/@ORG@/@REPO@/actions/workflows/vulncheck.yml)

# @REPO@

Collection of `.deb`/`.rpm` packages for World of Warships tools.

The repositories are available at: https://@ORG@.github.io/@REPO@/

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
wget -qO - https://@ORG@.github.io/@REPO@/GPG-KEY.pub | \
    ${SUDO} tee /etc/apt/keyrings/@REPO@.asc >/dev/null

# Add the repository
cat << EOF | ${SUDO} tee /etc/apt/sources.list.d/@REPO@.sources
Types: deb
URIs: https://@ORG@.github.io/@REPO@/deb.${VERSION_CODENAME}.${ARCH}/
Suites: ${VERSION_CODENAME}
Components: main
Architectures: ${ARCH}
Signed-By: /etc/apt/keyrings/@REPO@.asc
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

[@REPO@]
name=@REPO@
baseurl=https://@ORG@.github.io/@REPO@/rpm.${DISTRO_PREFIX}\$releasever.\$basearch/\$releasever/\$basearch/
enabled=1
gpgcheck=1
gpgkey=https://@ORG@.github.io/@REPO@/GPG-KEY.pub
EOF
```

## Build The `.rpm`/`.deb` Repositories

This project uses [Pakste](https://github.com/kakwa/pakste).

Check the [Pakste Documentation](https://kakwa.github.io/pakste/) for more details.
