# Mini-Facebook-docker

Open protocols and ports between the hosts
The following ports must be available. On some systems, these ports are open by default.

TCP port 2377 for cluster management communications
TCP and UDP port 7946 for communication among nodes
UDP port 4789 for overlay network traffic

to open port2377/tcp: firewall-cmd --add-port 2377/tcp


sudo docker swarm init
Swarm initialized: current node (btwe28qb9vg3qva8z8guxa3q9) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-26x50ymngw5bt1umugr5eyu0u9jvw3oj17423kihf2icbtyf1k-cyi6oeiebv7wb1yg5huywpmp3 10.100.104.32:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
