import pytest
import random
from main import dex_mod, hit_chance

@pytest.mark.parametrize('params, expected', [
    (8,-1),
    (9,-1),
    (10,0),
    (11,0),
    (12,1),
    (13,1),
    (14,2),
    (15,2),
    (16,3),
    (17,3),
    (18,4),
    (7,-2),
    (6,-2),
    (0,-5),
    (1,-5),
    (-1,-6)
    
])
def test_dex_mod(params, expected):
    assert dex_mod(params) == expected


@pytest.mark.parametrize('modifi, master_bonus, expected_hit', [
    (0,0,4),
    (1,0,5),
    (1,1,6),
    (0,2,6),
    (0,3,7),
    (2,2,8),
    (3,3,10),
    (4,1,9),
    (5,0,9),
    (-1,0,3),
    (-2,0,2),
])
def test_hit_chance(modifi, master_bonus, expected_hit):
    random.seed(42)
    assert hit_chance(modifi, master_bonus) == expected_hit


