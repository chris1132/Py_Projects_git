from functools import reduce
import numpy as np
class Node(object):
    def __init__(self,layer_index,node_index):
        self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.upstream = []
        self.output = 0
        self.delta = 0

    def set_output(self,output):
        self.output = output

    #add pre node
    def append_downstream_connection(self,conn):
        self.downstream.append(conn)

    #add next node
    def append_upstream_connection(self,conn):
        self.upstream.append(conn)

    #cal output
    def calc_output(self):
        output = reduce(lambda ret,conn: ret + conn.upstream_node.output * conn.weight,self.upstream,0)
        self.output =sigmoid(output)

    def calc_hidden_layer_delta(self):
        downstream_delta = reduce(lambda ret,conn: ret+conn.downstream_node.delta * conn.weight,self.downstream,0.0)
        self.delta = self.output * (1-self.output)*downstream_delta

    def calc_output_layer_delta(self,label):
        self.delta = self.output * (1-self.output)*(label - self.output)

    def __str__(self):
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.output, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        upstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.upstream, '')
        return node_str + '\n\tdownstream:' + downstream_str + '\n\tupstream:' + upstream_str

def sigmoid(x):
    return 1.0/(1+np.exp(-x))