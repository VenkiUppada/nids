"""
Signature-Based Intrusion Detection Rules
"""

def signature_detect(features):
    """
    features: dict with keys
    - packet_size
    - src_port
    - dst_port
    - protocol
    """

    packet_size = features.get("packet_size", 0)
    src_port = features.get("src_port", 0)
    dst_port = features.get("dst_port", 0)
    protocol = features.get("protocol", 0)

    # Rule 1: Large packet size (DoS / Flood)
    if packet_size > 1500:
        return "DoS Attack"

    # Rule 2: Port scanning (common ports)
    suspicious_ports = [21, 22, 23, 25, 80, 443, 3389]
    if dst_port in suspicious_ports:
        return "Port Scan"

    # Rule 3: ICMP flood
    if protocol == 1:
        return "ICMP Flood"

    return "Normal"
