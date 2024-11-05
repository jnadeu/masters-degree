import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('foo', 'bar')
print("Key foo contains", r.get('foo'))


redis-cli -p 7000 shutdown

# find the IDs of our shards by running the cluster nodes
redis-cli -p 7000 cluster nodes

# Add new primary node 7006
redis-cli --cluster add-node 127.0.0.1:7006 127.0.0.1:7000

# Add new slave node 7007
redis-cli -p 7000 --cluster add-node 127.0.0.1:7007 127.0.0.1:7000 --cluster-slave --cluster-master-id deb57b45c89063bca3a4471517c284286711eb9d


# Add new nodes
redis-cli --cluster add-node 127.0.0.1:7001 127.0.0.1:7000 --cluster-slots 0-8191
redis-cli --cluster add-node 127.0.0.1:7001 127.0.0.1:7000 --cluster-slots 8192-16383

# Remove a node 
redis-cli -p 7000 cluster forget 40fc1f91cf431fb8d5af578a3bb9a32cb4e4a9fb

# Create the cluster with 8 nodes (4 primary and 4 slaves)
redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 \
127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 \
127.0.0.1:7006 127.0.0.1:7007 --cluster-replicas 1

# Connect to node with cluster mode
redis-cli -c -p 7001

#---------------------------
ZADD lab1 7 Alice 7 Bob 6 Charlie
# Lab 2 grades
ZADD lab2 8 Alice 7 Bob 7 Charlie

# Lab 3 grades
ZADD lab3 9 Alice 8 Bob 6 Charlie

ZUNIONSTORE final_grade 3 lab1 lab2 lab3 WEIGHTS 0.2 0.2 0.6

ZRANGE final_grade 0 -1 WITHSCORES
