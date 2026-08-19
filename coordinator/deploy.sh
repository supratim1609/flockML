#!/usr/bin/env bash
set -e

echo "=========================================================================="
echo " 🚀 FlockML Sovereign AI — NIC/MeitY Coordinator Deployment Script"
echo "=========================================================================="

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 1. Check prerequisites
echo "[1/5] Checking deployment prerequisites..."
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed on this VM. Please install Docker first."
    exit 1
fi

# 2. Setup SSL Certs Directory
echo "[2/5] Setting up SSL certificates..."
mkdir -p certs
if [ ! -f certs/server.crt ] || [ ! -f certs/server.key ]; then
    echo "⚠️  No SSL certificates found in ./certs/. Generating 365-day self-signed TLS cert..."
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout certs/server.key \
        -out certs/server.crt \
        -subj "/C=IN/ST=Delhi/L=NewDelhi/O=MeitY/OU=NIC AI Division/CN=flockml.sovereign.local"
    echo "✅ Self-signed SSL certificates created in ./certs/."
else
    echo "✅ Using existing SSL certificates in ./certs/."
fi

# 3. Build & Launch Docker Containers
echo "[3/5] Building and launching FlockML Coordinator containers..."
if command -v docker-compose &> /dev/null; then
    docker-compose up -d --build
else
    docker compose up -d --build
fi

# 4. Systemd Registration (Optional if root)
echo "[4/5] Checking systemd service integration..."
if [ "$EUID" -eq 0 ]; then
    echo "Configuring systemd service..."
    mkdir -p /opt/flockml-coordinator
    cp -r ./* /opt/flockml-coordinator/
    cp flockml-coordinator.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl enable flockml-coordinator.service
    echo "✅ Systemd service 'flockml-coordinator.service' enabled."
else
    echo "ℹ️  Non-root user detected. Skipping systemd service auto-install."
fi

# 5. Verify Health Endpoint
echo "[5/5] Verifying Coordinator health endpoint..."
sleep 3
if curl -s http://localhost:8080/health | grep -q "healthy"; then
    echo "=========================================================================="
    echo " 🎉 FLOCKML COORDINATOR SERVER SUCCESSFULLY DEPLOYED & ONLINE!"
    echo " 📡 WSS Proxy Endpoint:   wss://<SERVER_IP>/ws"
    echo " 🩺 Health Check:          http://localhost:8080/health"
    echo " 📊 Live Metrics API:      http://localhost:8080/metrics"
    echo "=========================================================================="
else
    echo "⚠️  Coordinator container started, but health check pending. Run 'docker logs flockml-coordinator' to inspect logs."
fi
