#!/bin/bash
# High-reliability fetch for Stitch HTML (handles redirects and TLS).
# Usage: ./fetch-stitch.sh "<htmlCode.downloadUrl>" "temp/source.html"
set -e
URL=$1
OUTPUT=$2
if [ -z "$URL" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: $0 <url> <output_path>" >&2
  exit 1
fi
echo "Fetching Stitch HTML..." >&2
curl -L -f -sS --connect-timeout 10 --compressed "$URL" -o "$OUTPUT"
echo "Saved to: $OUTPUT" >&2
