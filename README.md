## Kubernetes setup
 
For this project, I have selected **K3s** for the Kubernetes cluster. K3s is considered a "batteries included distribution" as it comes prepackaged with an ingress controller, storage provisioner and more right out of the box. I have replaced Flannel CNI plugin with [Cilium](https://cilium.io/) to use [layer 2 announcements](https://docs.cilium.io/en/latest/network/l2-announcements/) feature. Cilium will assing IP addresses from a pool of addresses for service with type Loadbalancer and advertise the IP adderess on the local network. As a result, service running inside the cluster can be accessed externally.

## TODO
 - [x] write Ansible playbook to install K3s and required binaries
 - [ ] write Terraform module to create ec2 instances to run this project