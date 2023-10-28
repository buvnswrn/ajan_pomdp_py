import pomdp_py


class AJANOOBelief(pomdp_py.OOBelief):
    def __init__(self, agent_id, object_beliefs):
        self.agent_id = agent_id
        super().__init__(object_beliefs)


def initialize_belief(p_id: int, belief_dict: dict, representation):
    if representation == "histogram":
        oo_hists = {}
        for objcls in belief_dict[p_id].keys():
            total_prob = 0
            for state in belief_dict[p_id][objcls].keys():
                total_prob += belief_dict[p_id][objcls][state]

            for state in belief_dict[p_id][objcls]:
                belief_dict[p_id][objcls][state] /= total_prob
            hist_belief = pomdp_py.Histogram(belief_dict[p_id][objcls])
            oo_hists[ord(objcls[0])] = hist_belief
        return AJANOOBelief(p_id, oo_hists)
