# Name of the package
NAME = wows-extractor-gui

# Version
VERSION = 1.0.0

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

# Git revisions for each component. Update with: make manifest
REVISION             = main
REVISION_DEPACK      = main
REVISION_MODEL_EXP   = main

# Including common rules and targets
include buildenv/Makefile.common

# wows-extractor-gui submodules use SSH URLs and pinned commits that may not
# be publicly accessible, so we fetch each component independently via HTTPS.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(GS) -u $(URL) -o $(BUILD_DIR)/extractor-gui-src.tar.gz -r $(REVISION)
	tar -xzf $(BUILD_DIR)/extractor-gui-src.tar.gz -C $(SOURCE_DIR) --strip-components=1
	$(GS) -u https://github.com/wows-tools/wows-depack -o $(BUILD_DIR)/wows-depack-src.tar.gz -r $(REVISION_DEPACK)
	tar -xzf $(BUILD_DIR)/wows-depack-src.tar.gz -C $(SOURCE_DIR)/wows-depack --strip-components=1
	$(GS) -u https://github.com/wows-tools/wows-model-exporter -o $(BUILD_DIR)/wows-model-exporter-src.tar.gz -r $(REVISION_MODEL_EXP)
	tar -xzf $(BUILD_DIR)/wows-model-exporter-src.tar.gz -C $(SOURCE_DIR)/wows-model-exporter --strip-components=1
	$(SOURCE_TAR_CMD)
