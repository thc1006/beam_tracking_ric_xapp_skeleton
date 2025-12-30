from beam_tracking.schemas import Observation, Action

def test_observation_validation():
    obs = Observation(ue_id="imsi-1", rsrp_vector=[-90,-88,-95], prev_beam_id=0)
    assert obs.ue_id == "imsi-1"

def test_action_validation():
    a = Action(target_beam_id=1, confidence=0.5)
    assert a.target_beam_id == 1
