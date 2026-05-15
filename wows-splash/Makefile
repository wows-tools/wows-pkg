# Name of the package
NAME = wows-splash

# Version
VERSION = 0.1.0

# Revision number
RELEASE = 1

# URL of the project
URL=https://github.com/wows-tools/wows-splash/

# short summary of what the package provides
SUMMARY=World of Warships splash file parser

# long version of the summary
DESCRIPTION=wows-splash is a tool and library for parsing World of Warships .splash files, which describe ship hitbox geometry.

LICENSE=MIT

###############################################################################
# Rule #
########

# Including common rules and targets
include buildenv/Makefile.common

URL_SRC=$(URL)/archive/$(VERSION).tar.gz

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE)
