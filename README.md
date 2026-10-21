# Kubernetes Order Platform POC

A local, production-oriented Kubernetes and Elastic Stack proof of concept built to demonstrate practical DevOps and cloud platform engineering skills.

## Current Architecture

Windows 11
→ WSL2 Ubuntu
→ Docker Desktop
→ k3d
→ K3s

The platform will host:

- A Python/Flask order API
- Kubernetes-native deployment and security controls
- Elasticsearch
- Kibana
- Elastic Agent for Kubernetes container log collection
- Controlled failure scenarios for incident investigation

## Goals

- Reproducible local Kubernetes environment
- Resource-constrained Elastic Stack
- Structured application logging
- Kubernetes security fundamentals
- Observability and incident investigation
- GitHub-publishable implementation
- Clear evolution path from local K3s to Azure AKS

## Initial Version Baseline

| Component | Version |
|---|---|
| Kubernetes client | v1.36.1 |
| k3d | v5.9.0 |
| K3s | v1.35.5-k3s1 |
| Helm | v4.2.4 |
| ECK | v3.3.0 |
| Elasticsearch | 9.2.0 |
| Kibana | 9.2.0 |

## Status

Phase 1: Local Kubernetes platform — complete

Phase 2: Elastic Stack foundation — in progress
