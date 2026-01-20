from rules import signature_detect

test_cases = [
    {"packet_size": 2000, "dst_port": 80, "protocol": 6},
    {"packet_size": 500, "dst_port": 22, "protocol": 6},
    {"packet_size": 300, "dst_port": 1234, "protocol": 1},
    {"packet_size": 300, "dst_port": 1234, "protocol": 6},
]

for t in test_cases:
    print(t, "→", signature_detect(t))
