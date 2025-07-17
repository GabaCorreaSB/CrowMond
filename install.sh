#!/bin/bash
#
# Copyright (c) 2025 Gabriel Correa dos Santos Barbosa
# All rights reserved.
#
# Oh My Zsh–style installer for CrowdMon Grafana Edition

set -e

REPO_URL="https://github.com/GabaCorreaSB/crowdmon-grafana"
INSTALL_DIR="$HOME/.crowdmon-grafana"

echo "🚀 Installing CrowdMon Grafana Edition by Gabriel Correa dos Santos Barbosa..."

if [ -d "$INSTALL_DIR" ]; then
  echo "⚠️  $INSTALL_DIR already exists. Please remove it or run manually."
  exit 1
fi

echo "[*] Cloning repository..."
git clone "$REPO_URL" "$INSTALL_DIR"

echo "[*] Running setup..."
cd "$INSTALL_DIR"
chmod +x setup.sh
./setup.sh
