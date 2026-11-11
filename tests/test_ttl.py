from app.ttl import calculate_ttl_seconds


def test_ttl_5_minutes():
    assert calculate_ttl_seconds(5) == 300
