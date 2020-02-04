The following are the basic API that might help you be more productive when using the APIs on the Cisco DNA Center Platform

    https://{}/api/system/v1/auth/token Gets and encapsulates user identity and role information as a single value that RBAC-governed APIs use to make access-control decisions.
    https://{}/api/v1/network-device Gets the list of first 500 network devices sorted lexicographically based on host name. It can be filtered using management IP address, mac address, hostname and location name.
    https://{}/api/v1/interface Gets every interface on every network device. Whilst you can get a list of all interfaces via an API call, it is often more useful to get a subset of them. For example those that are attached to a specific network-device.
    https://{}/api/v1/host You can use the host API to get the name of a host, the ID of the VLAN that the host uses, the IP address of the host, the MAC address of the host, the IP address of the network device to which host is connected, and more.
    https://{}/api/v1/flow-analysis The path trace endpoint API to trace a path between two IP addresses. The function will wait for analysis to complete, and return the results
