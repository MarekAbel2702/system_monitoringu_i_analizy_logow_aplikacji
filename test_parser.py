from parse_logs import parse_log_line

with open("data/sample_logs.log", "r") as file:
    for line in file:
        result = parse_log_line(line)
        if result:
            print(f"✅ {result}")
        else:
            print(f"❌ Nie udało się sparsować: {line}")