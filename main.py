
def analyze_logs(file):
    failed_attempts = {}

    with open(file, "r") as f:
        for line in f:
            if "Failed login" in line:
                ip = line.strip().split()[-1]

                if ip not in failed_attempts:
                    failed_attempts[ip] = 0

                failed_attempts[ip] += 1

    print("\n Suspicious Activity Report:\n")

    for ip, count in failed_attempts.items():
        if count >= 2:
            print(f"IP {ip} has {count} failed login attempts!")

if __name__ == "__main__":
    analyze_logs("sample.log")
