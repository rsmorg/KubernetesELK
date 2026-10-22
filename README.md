# Kubernetes Elastic Observability Platform for Orders - POC

This is local, production-oriented Kubernetes and Elastic Stack proof of concept built to test various ways to implement K8s and EL. The idea for this POC was born out of the need to build production-like environment in a low to zero cost, on-prem, local set up that eventually be adapted to cloud. 

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
- Kibana visualizations and charts 
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

Phase 1: Local Kubernetes & Elastic platform — complete

Phase 2: Refining and securing the platform - in progress
