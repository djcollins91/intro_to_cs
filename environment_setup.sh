#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Checking for Homebrew..."

if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

echo "Updating Homebrew..."
brew update

echo "Installing Python 3..."
brew install python

echo "Installing Git..."
brew install git

echo "Python version:"
python3 --version

echo "Pip version:"
pip3 --version

echo "Git version:"
git --version

echo "Installation complete!"

