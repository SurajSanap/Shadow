# Here Restrict or allow access based on agent level and query type
RESTRICTED_LEVELS = {
    "Project Eclipse": 5,
    "Operation Void": 5,
    "Safehouse K-41": 2,
    "Facility X-17": 4,
    "Protocol Zeta": 5,
    "deepfake technology": 5,
    "Sleeper agent activation": 3,
    "Project Requiem": 5
}

def is_authorized(agent_level: int, query: str) -> bool:
    """
    Verifies if an agent is allowed to access the requested intel based on hardcoded clearance.
    """
    for keyword, min_level in RESTRICTED_LEVELS.items():
        if keyword.lower() in query.lower() and agent_level < min_level:
            return False
    return True

def deny_response():
    return "Access Denied – Clearance Insufficient."
