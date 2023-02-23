import sys
import multiprocessing as mp
import subprocessing as sp

def run_mapred(map_fn="wordcount_map.py", reduce_fn="wordcount_reduce.py", input_file="wonder.txt", output_loc="output.txt", num_mappers=2,
        num_reducers=2):
    for i in range(num_mappers):
        sp.Popen(['python', 'map_node.py'])

    for i in range(num_reducers):
        sp.Popen(['python', 'reduce_node.py'])

    

