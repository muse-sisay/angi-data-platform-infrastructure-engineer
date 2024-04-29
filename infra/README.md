# Installation
To setup a machine either a shell script or an Ansible playbook can be used. The script/playbook will install
- and configure k3s
- Cilium as the CNI with L2 IPAM and announcement
- ArgoCD and Argo Workflows
- Helm and Cilium binaries for installing charts and check Cilium status
- ArgoCD application to sync 

To use the shell script

```shell
git clone https://gitea.gc.home.arpa/black_sage/angi-data-platform-infrastructure-engineer.git
cd angi-data-platform-infrastructure-engineer/infra
bash setup.sh
```

Before using the Ansible playbook update the IP address and username in the inventory file.
```shell
ansible-playbook -i inventory.ini main.yml --ask-become-pass
```

# Configuration
## IPAM
The list of IP addresses that Cilium hands out to services of type Loadbalancer is defined in [CiliumLoadBalancerIPPool](../charts/cilium/templates/ciliumLoadBalancerIPPool.yaml) resource. The value is exposed through `ipRange` field in the Helm Chart. It accepts a start and end IP address range. To get add addresses assigned to services run
```shell
kubectl get svc -A | grep LoadBalancer
```

## ArgoCD access 
The default credentials for accessing ArgoCD UI is `admin/argocd`. The password is defined [here](../charts/argo-cd/dev-angi-01.yaml)