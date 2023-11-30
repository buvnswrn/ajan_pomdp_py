from rdflib import URIRef, Namespace

pomdp_ns = Namespace("http://www.dfki.de/pomdp-ns#")
pomdp_ns1 = Namespace("http://www.dfki.de/pomdp-ns/POMDP/")
pomdp_data_ns = Namespace("http://www.dfki.de/pomdp-ns/POMDP/data/")
POMDP = URIRef("http://www.dfki.de/pomdp-ns#POMDP")

_OOState = pomdp_ns["OOState"]
_State = pomdp_ns["State"]
_Action = pomdp_ns["Action"]
_Observation = pomdp_ns["Observation"]
_Reward = pomdp_ns["Reward"]
_TransitionFunction = pomdp_ns["TransitionFunction"]
_ObservationFunction = pomdp_ns["ObservationFunction"]
_RewardFunction = pomdp_ns["RewardFunction"]
_Policy = pomdp_ns["Policy"]
_Belief = pomdp_ns["Belief"]
_BeliefState = pomdp_ns["BeliefState"]

_Type = pomdp_ns["type"]
_Id = pomdp_ns["id"]
_Name = pomdp_ns["name"]
_Attributes = pomdp_ns["attributes"]
_NextState = pomdp_ns["next_state"]
_CurrentState = pomdp_ns["current_state"]
_CurrentAction = pomdp_ns["current_action"]
_Probability = pomdp_ns["probability"]
_CurrentObservation = pomdp_ns["CurrentObservation"]
_Pandas = pomdp_data_ns["pandasDataFrame"]


def createIRI(namespace, _id):
    return URIRef(str(namespace).replace("#", "/") + "_" + str(_id))
