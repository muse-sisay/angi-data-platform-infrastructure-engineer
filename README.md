## Kubernetes setup
 
For this project, I have selected **K3s** as the Kubernetes distribution. K3s is considered a "batteries included" as it comes prepackaged with an ingress controller and storage provisioner right out of the box. Rather than using the default Flannel CNI plugin, for this project I will be deploying [Cilium](https://cilium.io/) instead. By deploying Cilium as the CNI, services running in the cluster can be reached from outside the cluster using [layer 2 announcements](https://docs.cilium.io/en/latest/network/l2-announcements/), fulfilling an important role held by [cloud controller](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) in a managed Kubernetes or Cloud based deployments.


## TODO
 - [x] write Ansible playbook to install K3s and required binaries
 - [ ] write Terraform module to create ec2 instances to run this project