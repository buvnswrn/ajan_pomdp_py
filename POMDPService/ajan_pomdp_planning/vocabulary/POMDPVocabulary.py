from rdflib import URIRef, Namespace

pomdp_ns = Namespace("http://www.dfki.de/pomdp-ns#")
pomdp_ns1 = Namespace("http://www.dfki.de/pomdp-ns/POMDP/")
pomdp_data_ns = Namespace("http://www.dfki.de/pomdp-ns/POMDP/data/")
POMDP = URIRef("http://www.dfki.de/pomdp-ns#POMDP")
_rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')

_OOState = pomdp_ns["OOState"]
_State = pomdp_ns["State"]
_Action = pomdp_ns["Action"]
_Observation = pomdp_ns["Observation"]
_Reward = pomdp_ns["Reward"]
_Environment = pomdp_ns["Environment"]
_TransitionFunction = pomdp_ns["TransitionFunction"]
_ObservationFunction = pomdp_ns["ObservationFunction"]
_RewardFunction = pomdp_ns["RewardFunction"]
_Policy = pomdp_ns["Policy"]
_Belief = pomdp_ns["Belief"]
_BeliefState = pomdp_ns["BeliefState"]
_PlannedAction = pomdp_ns["plannedAction"]

_Type = pomdp_ns["type"]
_Id = pomdp_ns["id"]
_Name = pomdp_ns["name"]
_Attributes = pomdp_ns["attributes"]
_NextState = pomdp_ns["next_state"]
_CurrentState = pomdp_ns["current_state"]
_CurrentAction = pomdp_ns["current_action"]
_CurrentReward = pomdp_ns["current_reward"]
_Probability = pomdp_ns["probability"]
_CurrentObservation = pomdp_ns["CurrentObservation"]

_To_Print = pomdp_ns["to_print"]
_For_Hash = pomdp_ns["for_hash"]

_ObservationModel = pomdp_ns["ObservationModel"]
_TransitionModel = pomdp_ns["TransitionModel"]
_RewardModel = pomdp_ns["RewardModel"]
_PolicyModel = pomdp_ns["PolicyModel"]

# Datatypes
_Pandas = pomdp_data_ns["pandasDataFrame"]
_2dVector = pomdp_data_ns["2dVector"]
_3dVector = pomdp_data_ns["3dVector"]
_4dVector = pomdp_data_ns["4dVector"]

_Point = pomdp_data_ns["Point"]
# Action Selector is not needed.


def createIRI(namespace, _id):
    return URIRef(str(namespace).replace("#", "/") + "_" + str(_id))
