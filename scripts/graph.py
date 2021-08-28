from causalnex.structure.notears import from_pandas,from_pandas_lasso
from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE


class CausalGraph:
  def __init__(self,data,remove_nodes=None,with_constraints=False,use_lasso=True):
    self.lasso=use_lasso
    self.data = data
    self.remove_nodes = remove_nodes
    self.with_constraints = with_constraints
    self.make_graph()

  def make_graph(self):
    if self.with_constraints:
      self.construct_graph_with_constraints()
    elif self.remove_nodes is not None:
      self.construct_graph_removed_nodes()
    else:
      self.construct_graph()
    

  def construct_graph(self):
    if self.lasso:
      self.sm = from_pandas_lasso(self.data,beta=0.8)
    else:
      self.sm = from_pandas(self.data,beta=0.8)

  def construct_graph_removed_nodes(self):
    if self.lasso:
      self.sm = from_pandas_lasso(self.data, tabu_parent_nodes=self.remove_nodes, beta=0.8)
    else:
      self.sm = from_pandas(self.data, tabu_parent_nodes=self.remove_nodes,w_threshold=0.8)


  def construct_graph_with_constraints(self,constraints):
    if self.lasso:
      self.sm = from_pandas_lasso(self.data, tabu_edges==constraints, beta=0.8)
    else:
      self.sm = from_pandas(self.data, tabu_edges==constraints,w_threshold=0.8)

  def remove_weak_edges(self,thresh_val=0.8):
    self.sm.remove_edges_below_threshold(thresh_val)

  def return_sm(self):
    return self.sm

  def plot_graph(self,scale_value="2.0",size_value=2.5):     
    viz = plot_structure(
        self.sm,
        graph_attributes={"scale": scale_value, 'size':size_value},
        all_node_attributes=NODE_STYLE.WEAK,
        all_edge_attributes=EDGE_STYLE.WEAK)
    return Image(viz.draw(format='png'))

def jaccard_similarity(graph1, graph2):
    i = set(g).intersection(h)
    return round(len(i) / (len(g) + len(h) - len(i)),3)

jaccard_similarity(graph1.edges(), graph2.edges())