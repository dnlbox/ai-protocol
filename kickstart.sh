#!/usr/bin/env bash
set -e

# Default repository to pull the template from.
# Update this if you fork the project!
REPO_URL="https://github.com/dnlbox/ai-protocol.git"
TARGET_DIR="${1:-my-ai-project}"

if [ -d "$TARGET_DIR" ]; then
  echo "Error: Directory '$TARGET_DIR' already exists. Please choose a different name."
  exit 1
fi

echo "Scaffolding Agnostic Agentic Reasoning Environment in '$TARGET_DIR'..."

# Create a temporary directory
TMP_DIR=$(mktemp -d)

# Clone the repository (depth=1 for speed)
git clone --depth 1 "$REPO_URL" "$TMP_DIR" --quiet

# Copy the full template, including hidden entries like .agents. The trailing
# /. copies all contents (dotfiles included) without pulling in the parent dir,
# avoiding the ".*" glob footgun that also matches "..".
mkdir -p "$TARGET_DIR"
cp -R "$TMP_DIR/template/." "$TARGET_DIR/"

# Clean up
rm -rf "$TMP_DIR"

echo "=========================================================================="
echo "Scaffold complete."
echo "Open docs/concept/, write down what you want to build,"
echo "and ask your AI to /sync-protocols when you are ready to lock in a tech stack."
echo "=========================================================================="
