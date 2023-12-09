import rdflib
import rdfpandas
from numpy import ndarray
from pandas import DataFrame
from rdflib import Graph, RDF, BNode, Literal
from rdflib.term import Node, URIRef
from typing import Union, Any

from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import _rdf, _2dVector, _3dVector, _Pandas, createIRI, \
    _Point


def parse_pandas(graph, o):
    # TODO: Implement pandas dataframe parsing
    pass


def from_2dVector(graph: Graph, o) -> tuple:
    x_value = [x for _, _, x in graph.triples((o, _rdf.x, None))][0]
    y_value = [x for _, _, x in graph.triples((o, _rdf.y, None))][0]
    x_value = get_data_from_graph(x_value)
    y_value = get_data_from_graph(y_value)
    return x_value, y_value


def from_3dVector(graph: Graph, vector_node) -> tuple:
    x_value, y_value = from_2dVector(graph, vector_node)
    z_value = [x for _, _, x in graph.triples((vector_node, _rdf.z, None))][0]
    z_value = get_data_from_graph(z_value)
    return x_value, y_value, z_value


def to_2dVector(graph: Graph, x, y) -> BNode:
    vector_value = BNode()
    graph.add((vector_value, RDF.type, _2dVector))
    graph.add((vector_value, _rdf.x, get_value_to_graph_literal(x)))
    graph.add((vector_value, _rdf.y, get_value_to_graph_literal(y)))
    return vector_value


def to_3dVector(graph: Graph, x, y, z) -> BNode:
    vector_value = BNode()
    graph.add((vector_value, RDF.type, _3dVector))
    graph.add((vector_value, _rdf.x, get_value_to_graph_literal(x)))
    graph.add((vector_value, _rdf.y, get_value_to_graph_literal(y)))
    graph.add((vector_value, _rdf.z, get_value_to_graph_literal(z)))
    return vector_value


def to_GraphDataFrame(graph: Graph, df: DataFrame, row_name_starter: URIRef = None,
                      column_name_starter: URIRef = None) -> Node:
    df_value = BNode()
    graph.add((df_value, RDF.type, _Pandas))
    row_dim, col_dim = df.shape
    if col_dim == 1:
        df.columns = [RDF.value] if column_name_starter is None else [column_name_starter]
    elif col_dim == 2:
        df.columns = [_rdf.x, _rdf.y]
    elif col_dim == 3:
        df.columns = [_rdf.x, _rdf.y, _rdf.z]

    row_value = BNode()
    for i in range(row_dim):
        graph.add((row_value, RDF.value, createIRI(_Point if row_name_starter is None else row_name_starter, i)))
    graph.add((df_value, RDF.value, row_value))

    df.index = [createIRI(_Point, i) for i in range(row_dim)]

    g = rdfpandas.to_graph(df)
    graph += g

    return df_value


def get_data_from_graph(o: Union[Literal, BNode, Any], graph: Graph = None) -> Union[
    ndarray, DataFrame, str, int, float, bool, tuple, None]:
    if type(o) is Literal:
        dt = rdflib.term.XSDToPython[o.datatype]
        if dt is not None:
            return dt(o)
        else:
            return str(o)
    elif type(o) is BNode:
        for _, _, data_type in graph.triples((o, RDF.type, None)):
            if data_type == _Pandas:
                return parse_pandas(graph, o)
            elif data_type == _2dVector:
                return from_2dVector(graph, o)
            elif data_type == _3dVector:
                return from_3dVector(graph, o)
    elif o == RDF.nil:
        return None
    else:
        return str(o)


def get_value_to_graph_literal(o, graph=None):
    if type(o) in [int, float, bool, str]:
        return Literal(o)
    elif o is None:
        return RDF.nil
    elif type(o) is tuple:
        if len(o) == 2:
            return to_2dVector(graph, o[0], o[1])
        elif len(o) == 3:
            return to_3dVector(graph, o[0], o[1], o[2])
        elif len(o) > 3:
            print("Tuple size is greater than 3")
            return Literal(o)
    elif type(o) is ndarray:
        return to_GraphDataFrame(graph, DataFrame(o))
    elif type(o) is DataFrame:
        return to_GraphDataFrame(graph, o)
    else:
        print("Unknown type")
        return Literal(o)
