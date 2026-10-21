#!/usr/bin/env bash

set -euo pipefail

kubectl create secret generic order-api-secret \
  --namespace application \
  --from-literal=ORDER_API_TOKEN=poc-demo-token \
  --dry-run=client \
  -o yaml | kubectl apply -f -

echo "Local order-api Secret created/updated."