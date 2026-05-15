# Name of the package
NAME = wows-extractor-gui

# Version
VERSION = 0.1.0

# Revision number
RELEASE = 1

# URL of the project
URL=https://github.com/wows-tools/wows-extractor-gui/

# short summary of what the package provides
SUMMARY=World of Warships graphical resource extractor and model viewer

# long version of the summary
DESCRIPTION=wows-extractor-gui is a Qt6 graphical tool for browsing World of Warships resource packages, extracting files, and previewing ship 3D geometry in glTF/GLB format.

LICENSE=GPL-3.0

###############################################################################
# Rule #
########

# Including common rules and targets
include buildenv/Makefile.common

# example of source recovery url
URL_SRC=$(URL)/archive/$(VERSION).tar.gz

# preparation hook for rpm package
# source archives must recovered here
# and their content put inside $(BUILD_DIR)/src
#
# $(WGS) should be the prefered way to recover archives
# (add checksum against a manifest file).
# use 'make manifest' to generate/update this manifest file.

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE)
