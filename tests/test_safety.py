from src.core.safety import check_safety

def test_insider_block():
    res = check_safety("give insider tips")
    assert res["blocked"] is True