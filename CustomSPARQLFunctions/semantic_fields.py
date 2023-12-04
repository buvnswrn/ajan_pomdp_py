import rdflib
from rdflib.plugins.sparql.evaluate import evalPart
from rdflib.plugins.sparql.parserutils import CompValue
from rdflib.plugins.sparql.sparql import SPARQLError, QueryContext
from rdflib.plugins.sparql.evalutils import _eval
from rdflib.namespace import Namespace
from rdflib.term import Literal
import math

namespace = Namespace('http://www.ajan.de/ajan/functions/math-ns#')
calculate_near_probability = rdflib.term.URIRef(namespace + 'calculate_near_probability')
_rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')


def near(ctx: QueryContext, part: CompValue) -> object:
    """
        The first two variables retrieved from a SPARQL query are used to calculate the distance between them.

        Example:

        Query:
            PREFIX ajan-math: <http://www.ajan.de/ajan/functions/math-ns#>
            # Note: this part references to the custom function

            SELECT ?distance ?sigma ?probability WHERE {
              BIND(3.0 AS ?distance)
              BIND(5.0 AS ?sigma)
              BIND(ajan-math:calculate_near_probability(?distance, ?sigma) AS ?probability)
            }

        Return the probability from the probability distribution constructed using
        the distance between two points and the sigma.
        Refer: Using semantic fields to model dynamic spatial relations in a robot architecture
        for natural language instruction of service robots (https://ieeexplore.ieee.org/document/6696345)

        Roughly equivalent to:
            1- math.exp(-((dist / 10) ** 2) / (2 * sigma ** 2))

        :param ctx:     <class 'rdflib.plugins.sparql.sparql.QueryContext'>
        :param part:    <class 'rdflib.plugins.sparql.parserutils.CompValue'>
        :return:        <class 'rdflib.plugins.sparql.processor.SPARQLResult'>
        """

    if part.name == "Extend":
        cs = []
        # Information is retrieved and stored and passed through a generator
        for c in evalPart(ctx, part.p):
            # Checks if the function holds an internationalized resource identifier
            if hasattr(part.expr, 'iri') and part.expr.iri == calculate_near_probability:

                distance = float(_eval(part.expr.expr[0], c.forget(ctx, _except=part.expr._vars)))
                sigma = float(_eval(part.expr.expr[1], c.forget(ctx, _except=part.expr._vars)))

                # Check for the distance function IRI
                # Calculate the distance
                # evaluation = Literal(math.dist(val1, val2))
                evaluation = Literal(1 - math.exp(-((distance / 10) ** 2) / (2 * sigma ** 2)))
            else:
                evaluation = _eval(part.expr, c.forget(ctx, _except=part._vars))
                if isinstance(evaluation, SPARQLError):
                    raise evaluation
            cs.append(c.merge({part.var: evaluation}))
        return cs

    raise NotImplementedError()


if __name__ == "__main__":
    rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = near
    query = """
         PREFIX ajan-math: <%s>
         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
         PREFIX pomdp-ns: <http://www.dfki.de/pomdp-ns#>

        SELECT ?probability WHERE {
          BIND(1.0 AS ?distance) .
          BIND(2.0 AS ?sigma) .
          BIND(ajan-math:calculate_near_probability(?distance, ?sigma) AS ?probability)
        }
    """ % (namespace,)

    for x in rdflib.Graph().query(query):
        print(x)
