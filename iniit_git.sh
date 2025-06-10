#!/bin/bash

set -e

# --- Configuration ---
REPO_NAME=${1:-"Into_To_CS"}
VISIBILITY=${2:-"private"}  # Options: private, public
INITIAL_COMMIT_MESSAGE=${3:-"Initial commit"}

# --- Check for gh CLI ---
if ! command -v gh &> /dev/null
then
    echo "GitHub CLI (gh) not found. Install it with: https://cli.github.com/"
    exit 1
fi

# --- Git setup ---
echo "Initializing Git repository..."
git init

echo "Adding all files..."
git add .

echo "Creating initial commit..."
git commit -m "$INITIAL_COMMIT_MESSAGE"

echo "Creating GitHub repo: $REPO_NAME ($VISIBILITY)..."
gh repo create "$REPO_NAME" --$VISIBILITY --source=. --remote=origin --push

echo "✅ Repo created and pushed to GitHub!"
