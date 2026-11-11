def calculate_ttl_seconds(ttl_minutes: int) -> int:
    """把 Agent 注册的 TTL（分钟）换算成秒。"""
    return ttl_minutes * 3600   # 缺陷：误把分钟当小时
