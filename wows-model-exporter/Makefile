# Name of the package
NAME = wows-model-exporter

# Version
VERSION = 0.2.0

# Revision number
RELEASE = 1

# URL of the project
URL=https://github.com/wows-tools/wows-model-exporter/

# short summary of what the package provides
SUMMARY=World of Warships 3D model exporter

# long version of the summary
DESCRIPTION=wows-model-exporter parses and exports World of Warships ship geometry to glTF/GLB format. It provides a library and command-line tools for accessing ship 3D models.

LICENSE=MIT

###############################################################################
# Rule #
########

# Git revision or branch for source checkout.
# Use 'make manifest' to pin to the current HEAD commit.
REVISION = main

# Including common rules and targets
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(GS) -u $(URL) -o $(SOURCE_ARCHIVE) -r $(REVISION)
