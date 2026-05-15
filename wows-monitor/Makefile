# Name of the package
NAME = wows-monitor

# Version (matches release/app/package.json)
VERSION = 1.3.4

# Revision number
RELEASE = 1

# URL of the project (upstream Azure DevOps repo)
URL=https://wows-monitor@dev.azure.com/wows-monitor/app/_git/app

# short summary of what the package provides
SUMMARY=Matchmaking monitor for World of Warships

# long version of the summary
DESCRIPTION=wows-monitor is a real-time companion application for World of Warships that displays current player statistics for allies and enemies during gameplay.

LICENSE=unknown

# Allow network inside chroot for npm install
COWBUILD_BUILD_ADDITIONAL_ARGS=--use-network yes

###############################################################################
# Rule #
########

# Git revision — release tag
REVISION = release/1.3.4

# Including common rules and targets
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(GS) -u $(URL) -o $(SOURCE_ARCHIVE) -r $(REVISION)
