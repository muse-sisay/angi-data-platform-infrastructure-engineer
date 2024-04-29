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
### IPAM
The list of IP addresses that Cilium hands out to services of type Loadbalancer is defined in [CiliumLoadBalancerIPPool](../charts/cilium/templates/ciliumLoadBalancerIPPool.yaml) resource. The value is exposed through `ipRange` field in the Helm Chart. It accepts a start and end IP address range. To get add addresses assigned to services run
```shell
kubectl get svc -A | grep LoadBalancer
```

### ArgoCD access 
The default credentials for accessing ArgoCD UI is `admin/argocd`. The password is defined [here](../charts/argo-cd/dev-angi-01.yaml).

### Data pipeline 
Chart for installing the data pipeline can be found [here](../charts/weather-cronjob/).
#### Change schedule
The schedule is defined in cron format. To change the schedule update `schedule` field in `/charts/weather-cronjob` chart and commit your change. ArgoCD will notice the change and reconcile the cluster state to match what is defined in git.

#### Change forecast location
The area where the script/pipline download forecast for is defined in `location` object.
```yaml
lolocation:
  # -- longitude
  longitude: -86.1551
  # -- latitude
  latitude: 39.7671
```
#### Deployment mode 
The pipeline can deployed as either a Kubernetes cronjob or Argo Cron Workflow. To choose set `controlMode` field.

### Trigger data pipeline manually
For the cron job deployment 
```shell
kubectl create job manual-run --from=cronjob/weather-forecast
```