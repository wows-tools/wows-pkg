[![Build Packages Repositories](https://github.com/wows-tools/wows-pkg/actions/workflows/repos.yml/badge.svg)](https://github.com/wows-tools/wows-pkg/actions/workflows/repos.yml)
[![Check CVEs on NVD](https://github.com/wows-tools/wows-pkg/actions/workflows/vulncheck.yml/badge.svg)](https://github.com/wows-tools/wows-pkg/actions/workflows/vulncheck.yml)


# wows-pkg

Collection of packages of my personal projects.

The `.deb`/`.rpm` repositories are available at the following url: https://wows-tools.github.io/wows-pkg/

## Ubuntu/Debian

If you are using `Ubuntu`/`Debian`, here how to install the repository:

```shell
# If you are not root
export SUDO=sudo

# Get your OS version
. /etc/os-release

# Add the GPG key
wget -qO - https://wows-tools.github.io/wows-pkg/GPG-KEY.pub | \
    gpg --dearmor | ${SUDO} tee /etc/apt/trusted.gpg.d/wows-pkg.gpg

# Add the repository
echo "deb [arch=$(dpkg --print-architecture)] \
https://wows-tools.github.io/wows-pkg/deb.${VERSION_CODENAME}.$(dpkg --print-architecture)/ \
${VERSION_CODENAME} main" | ${SUDO} tee /etc/apt/sources.list.d/wows-pkg.list

# update
apt update
```

# Building

Check the [pakste documention](https://kakwa.github.io/pakste/).
