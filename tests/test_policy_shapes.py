import torch
from beam_tracking.model.rsrp_student import RSRPStudentPolicy

def test_rsrp_student_shapes():
    m = RSRPStudentPolicy(n_beams=5)
    x = torch.randn(2,5)
    y = m(x)
    assert y.shape == (2,5)
