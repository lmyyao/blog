##### Veth Virtual Network Card

1. brctl addbr br0
2. ip link set br0 up
3. ip addr add 172.17.42.1/16 dev br0
4. ip netns add netns1
5. ip netns exec netns1 ip link set lo up
6. ip link add veth0 type veth peer name veth1
7. ip link set veth1 netns netns1
8. ip netns exec netns1 ip addr add 172.17.42.100/16 dev veth1
9. ip netns exec netns1 ip link set veth1 up
10. ip link set veth0 up
11. ip addr add 172.17.42.99/16 dev veth0
12. brctl addif br0 veth0
13. ip netns exec netns1 ip route add default via 172.17.42.1
14. iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
15. echo "nameserver 114.114.114.114" > /etc/netns/netns1/resolv.conf
