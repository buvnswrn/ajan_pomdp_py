import numpy as np
import rdflib
from rdflib import Graph
from rdflib.plugins.sparql.evaluate import evalPart
from rdflib.plugins.sparql.parserutils import CompValue
from rdflib.plugins.sparql.sparql import SPARQLError, QueryContext
from rdflib.plugins.sparql.evalutils import _eval
from rdflib.namespace import Namespace
from rdflib.term import Literal
import math

from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, pomdp_ns, _rdf

namespace = Namespace('http://www.ajan.de/ajan/functions/math-ns#')
math_distance = rdflib.term.URIRef(namespace + 'distance')
sample = rdflib.term.URIRef(namespace + 'sample')


def distance(ctx: QueryContext, part: CompValue) -> object:
    """
    The first two variables retrieved from a SPARQL query are used to calculate the distance between them.

    Example:

    Query:
        PREFIX ajan-math: <http://www.ajan.de/ajan/functions/math-ns#>     # Note: this part references to the custom function

        SELECT ?x ?y ?distance WHERE {
          BIND(1.0 AS ?x)
          BIND(2.0 AS ?y)
          BIND(ajan-math:distance(?x, ?y) AS ?distance)
        }

    Return the Euclidean distance between two points p and q.
    Roughly equivalent to:
        sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    :param ctx:     <class 'rdflib.plugins.sparql.sparql.QueryContext'>
    :param part:    <class 'rdflib.plugins.sparql.parserutils.CompValue'>
    :return:        <class 'rdflib.plugins.sparql.processor.SPARQLResult'>
    """

    if part.name == "Extend":
        cs = []
        # Information is retrieved and stored and passed through a generator
        for c in evalPart(ctx, part.p):
            # Checks if the function holds an internationalized resource identifier
            if hasattr(part.expr, 'iri'):
                # Check for the distance function IRI
                if part.expr.iri == math_distance:
                    points1 = _eval(part.expr.expr[0], c.forget(ctx, _except=part.expr._vars))  # point1
                    points2 = _eval(part.expr.expr[1], c.forget(ctx, _except=part.expr._vars))  # point2
                    graph: Graph = c.ctx.graph
                    point1 = []
                    point2 = []
                    for s, p, x in graph.triples((points1, _rdf.x, None)):
                        point1.append(float(x))
                    for s, p, y in graph.triples((points1, _rdf.y, None)):
                        point1.append(float(y))

                    for s, p, x in graph.triples((points2, _rdf.x, None)):
                        point2.append(float(x))
                    for s, p, y in graph.triples((points2, _rdf.y, None)):
                        point2.append(float(y))

                    # Calculate the distance
                    if len(point2) > 2 or len(point1) > 2:
                        print(graph.serialize(format='turtle'))
                    # Both points should have the same dimensionality
                    try:
                        evaluation = Literal(math.dist(point1, point2))
                    except ValueError:
                        raise ValueError("Both points should have the same dimensionality. \n Graph " + graph.serialize(
                            format='turtle'))
                    # evaluation = Literal(val1-val2)

                else:
                    # raise NotImplementedError() so other functions can execute
                    raise NotImplementedError()
            else:
                evaluation = _eval(part.expr, c.forget(ctx, _except=part._vars))
                if isinstance(evaluation, SPARQLError):
                    raise evaluation
            cs.append(c.merge({part.var: evaluation}))
        return cs

    raise NotImplementedError()


def sample_values(ctx: QueryContext, part: CompValue) -> object:
    """
    The first three variables retrieved from a SPARQL query are used to draw samples from a uniform distribution.

    Example:

    Query:
        PREFIX ajan-math: <http://www.ajan.de/ajan/functions/math-ns#>     # Note: this part references to the custom function

        SELECT ?low ?high ?distance WHERE {
          BIND(1.0 AS ?low)
          BIND(2.0 AS ?high)
          BIND(ajan-math:sample(?low, ?high) AS ?sample)
        }

    Return the Euclidean distance between two points p and q.
    Roughly equivalent to:
        sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    :param ctx:     <class 'rdflib.plugins.sparql.sparql.QueryContext'>
    :param part:    <class 'rdflib.plugins.sparql.parserutils.CompValue'>
    :return:        <class 'rdflib.plugins.sparql.processor.SPARQLResult'>
    """

    if part.name == "Extend":
        cs = []
        # Information is retrieved and stored and passed through a generator
        for c in evalPart(ctx, part.p):
            # Checks if the function holds an internationalized resource identifier
            if hasattr(part.expr, 'iri'):
                # Check for the distance function IRI
                if part.expr.iri == sample:
                    points1 = int(_eval(part.expr.expr[0], c.forget(ctx, _except=part.expr._vars)))  # low
                    points2 = int(_eval(part.expr.expr[1], c.forget(ctx, _except=part.expr._vars)))  # high
                    # TODO: Fix this one with the correct values.
                    #  i.e. the values should be in the range of reference points
                    x_values = np.random.uniform(points1, points2)
                    evaluation = Literal(x_values)

                else:
                    # raise NotImplementedError() so other functions can execute
                    raise NotImplementedError()
            else:
                evaluation = _eval(part.expr, c.forget(ctx, _except=part._vars))
                if isinstance(evaluation, SPARQLError):
                    raise evaluation
            cs.append(c.merge({part.var: evaluation}))
        return cs

    raise NotImplementedError()


if __name__ == "__main__":
    # add function directly, normally we would use setuptools and entry_points
    rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = distance
    rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = sample_values

    g = Graph()
    point1 = createIRI(pomdp_ns, "keypoint1")
    point2 = createIRI(pomdp_ns, "keypoint2")
    g.add((point1, _rdf.x, Literal(1.0)))
    g.add((point1, _rdf.y, Literal(2.0)))
    g.add((point2, _rdf.x, Literal(3.0)))
    g.add((point2, _rdf.y, Literal(4.0)))

    query = """
         PREFIX ajan-math: <%s>
         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
         PREFIX pomdp-ns: <http://www.dfki.de/pomdp-ns#>
         PREFIX pomdp-ns1: <http://www.dfki.de/pomdp-ns/>

        SELECT ?distance WHERE {
          BIND(ajan-math:distance(pomdp-ns1:_keypoint1, pomdp-ns1:_keypoint2) AS ?distance)
        }
    """ % (namespace,)
    # Find all FOAF Agents
    for x in g.query(query):
        print(x)
