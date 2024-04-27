#!/bin/bash
# setup.sh 
# Script for installing k3s on a linux mahchine

# check if script is run as privilages user. 
# If not, exit script
if [ "$EUID" -ne 0 ]
  then echo "Please run as sudo"
  exit
fi

mkdir -p /etc/rancher/k3s
cp ./k3s-config.yaml /etc/rancher/k3s/config.yaml
curl -sfL https://get.k3s.io | sh -

# export kubeconfig file
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml


# Install Helm, Cilium
# TODO: use device arch 
# Helm  v3.14.4
wget https://get.helm.sh/helm-v3.14.4-linux-amd64.tar.gz -P /tmp
tar -xvf /tmp/helm-v3.14.4-linux-amd64.tar.gz  --strip-components 1 -C /usr/bin linux-amd64/helm
rm /tmp/helm-v3.14.4-linux-amd64.tar.gz

# install cilium
wget https://github.com/cilium/cilium-cli/releases/download/v0.16.5/cilium-linux-amd64.tar.gz -P /tmp
tar xzvfC /tmp/cilium-linux-amd64.tar.gz /usr/local/bin
rm /tmp/cilium-linux-amd64.tar.gz


helm dependency update ../charts/cilium/
helm install cilium -n kube-system -f ../charts/cilium/dev-angi-01.yaml ../charts/cilium


helm dependency build ../charts/argo-cd/
helm install argocd -n argocd --create-namespace  -f ../charts/argo-cd/dev-angi-01.yaml ../charts/argo-cd

helm dependency build ../charts/argo-workflow/
helm install argocd -n workflow --create-namespace  -f ../charts/argo-workflow/dev-angi-01.yaml ../charts/argo-workflow