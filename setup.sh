#!/bin/bash
#
# Copyright (c) 2025 Gabriel Correa dos Santos Barbosa
# All rights reserved.

set -e

echo "[*] Starting CrowdMon (Grafana Edition)..."
docker-compose up -d --build

echo "[*] Waiting for exporter to initialize..."
sleep 10

echo ""
echo "✅ Services are running:"
echo "🛡️ CrowdSec API:   http://localhost:8080"
echo "📊 Grafana:        http://localhost:3000"
echo "   → Login: admin / admin"
echo ""
echo "📦 PostgreSQL stores your alerts. Exporter will feed Grafana automatically."
