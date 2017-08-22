# virsh 管理KVM


1. 创建镜像
`qemu-img create -f raw /mnt/fedora.img 10G`

2. Create Virtual Machines
`virt-install  -name=fedora --disk path=/mnt/fedora.img --vcpu=2 --ram=1024 --location=/mnt/Fedora-Server-dvd-x86_64-26-1.5.iso --network bridge=virbr0 --graphics spice`

3. start domain
`virsh start <domain name>`

4. connect domain
`virt-viewer <domain name>`

5. dumpxml 
`virsh dumpxml <domain name>`

6. shutdown domain
`virsh shutdown <domain name>`

7. destory domain
`virsh destroy <domain name>`

8. remove domain
`virsh undefine guest1 --remove-all-storage`
9. bridged network
`virt-install  -name=fedora2 --disk path=/mnt/fedora2.img --vcpu=2 --ram=1024 --location=/mnt/Fedora-Server-dvd-x86_64-26-1.5.iso --network bridge=vbr0 --graphics spice`
[Libvirt Networking handbook](https://jamielinux.com/docs/libvirt-networking-handbook/bridged-network.html#limitations)
