#!/bin/bash
# setup.sh 
# Script for installing k3s on a linux mahchine


mkdir -p /etc/rancher/k3s
cp ./k3s-config.yaml /etc/rancher/k3s/config.yaml
curl -sfL https://get.k3s.io | sh -

