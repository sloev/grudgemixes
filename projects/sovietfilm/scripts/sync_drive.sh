#!/usr/bin/env bash
set -euo pipefail

# Copy (never delete) local audio into the private sovietfilm Drive folder.
# Configure an rclone remote named sovietdrive first, or override RCLONE_REMOTE.
RCLONE_REMOTE="${RCLONE_REMOTE:-sovietdrive}"
DRIVE_FOLDER_ID="${DRIVE_FOLDER_ID:-1_l7vocHbIfgW0vkzuaNJGFUNSMRIszGQ}"
SOURCE_DIR="${1:-audio}"

command -v rclone >/dev/null 2>&1 || {
  echo "ERROR: rclone is not installed or not on PATH" >&2
  exit 2
}
[[ -d "$SOURCE_DIR" ]] || {
  echo "ERROR: audio source folder not found: $SOURCE_DIR" >&2
  exit 2
}

echo "Copying $SOURCE_DIR/ to ${RCLONE_REMOTE}: (Drive folder ${DRIVE_FOLDER_ID})"
rclone copy "$SOURCE_DIR" "${RCLONE_REMOTE}:" \
  --drive-root-folder-id "$DRIVE_FOLDER_ID" \
  --checksum --progress

echo "Remote inventory:"
rclone lsjson "${RCLONE_REMOTE}:" \
  --drive-root-folder-id "$DRIVE_FOLDER_ID" \
  --recursive
