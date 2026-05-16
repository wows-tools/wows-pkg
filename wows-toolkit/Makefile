# Name of the package
NAME = wows-toolkit

# Version (matches workspace Cargo.toml)
VERSION = 0.1.68

# Revision number
RELEASE = 1

# URL of the project
URL=https://github.com/landaire/wows-toolkit/

# short summary of what the package provides
SUMMARY=World of Warships tools suite

# long version of the summary
DESCRIPTION=wows-toolkit is a Swiss army knife for World of Warships, providing a GUI application and CLI tools for browsing replays, extracting game files, viewing armor models, and analysing replay data.

LICENSE=MIT

# Allow network inside chroot for rustup + cargo fetch
COWBUILD_BUILD_ADDITIONAL_ARGS=--use-network yes

SKIP=>=:deb:0 >=:el:0 >=:fc:0 >=:ubu:0.4


###############################################################################
# Rule #
########

# Git revision — uses the release tag
REVISION = v$(VERSION)

# Including common rules and targets
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(GS) -u $(URL) -o $(BUILD_DIR)/wows-toolkit-src.tar.gz -r $(REVISION)
	tar -xzf $(BUILD_DIR)/wows-toolkit-src.tar.gz -C $(SOURCE_DIR) --strip-components=1
	rm -rf $(SOURCE_DIR)/.git
	$(SOURCE_TAR_CMD)
