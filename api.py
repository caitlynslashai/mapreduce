import masternode as master

def cluster_id(num_mappers, num_reducers):
    return master.cluster_id(num_mappers, num_reducers)

def run_mapred(input_data, map_fn, reduce_fn, output_location,
        cluster_id=None):
    # note that run_mapred will send "lnum=#;jumps=#" as the first line of the
    # input to mappers
    
    # if cluster_id is left as None then run_mapred will create a new cluster
    # with 2 mappers and 2 reducers
    master.run_mapred(input_data, map_fn, reduce_fn, output_location,
            cluster_id)

def destroy_cluster(cluster_id):
    master.destroy_cluster(cluster_id)
