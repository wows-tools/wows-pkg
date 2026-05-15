# Name of the package
NAME = wows-fuse

# Version
VERSION = 0.1.0

# Revision number
RELEASE = 1

# URL of the project
URL=https://github.com/wows-tools/wows-fuse/

# short summary of what the package provides
SUMMARY=FUSE filesystem for World of Warships resource packages

# long version of the summary
DESCRIPTION=wows-fuse mounts World of Warships .idx/.pkg resource packages as a virtual FUSE filesystem, enabling exploration without manual extraction.

LICENSE=MIT

###############################################################################
# Rule #
########

# Including common rules and targets
include buildenv/Makefile.common

URL_SRC=$(URL)/archive/$(VERSION).tar.gz

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE)
