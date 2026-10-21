#!/usr/bin/env bash

set -euo pipefail

TLS_DIR="app/k8s/tls"

mkdir -p "$TLS_DIR"

echo "Generating local CA..."

openssl req -x509 -nodes -newkey rsa:4096 \
  -keyout "$TLS_DIR/ca.key" \
  -out "$TLS_DIR/ca.crt" \
  -days 825 \
  -subj "/C=NL/O=k8s-order-platform/OU=Local POC/CN=k8s-order-platform Local CA"

echo "Generating order-api private key and CSR..."

openssl req -nodes -newkey rsa:2048 \
  -keyout "$TLS_DIR/order-api.key" \
  -out "$TLS_DIR/order-api.csr" \
  -subj "/C=NL/O=k8s-order-platform/OU=Application/CN=order-api.k8s.local"

cat > "$TLS_DIR/order-api.ext" <<EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage=digitalSignature,keyEncipherment
extendedKeyUsage=serverAuth
subjectAltName=DNS:order-api.k8s.local
EOF

echo "Signing order-api certificate..."

openssl x509 -req \
  -in "$TLS_DIR/order-api.csr" \
  -CA "$TLS_DIR/ca.crt" \
  -CAkey "$TLS_DIR/ca.key" \
  -CAcreateserial \
  -out "$TLS_DIR/order-api.crt" \
  -days 825 \
  -sha256 \
  -extfile "$TLS_DIR/order-api.ext"

echo
echo "TLS files generated under $TLS_DIR"
echo
echo "Public certificates:"
echo "  $TLS_DIR/ca.crt"
echo "  $TLS_DIR/order-api.crt"
echo
echo "Private files are ignored by Git."