import psutil
import time
import logging
from datetime import datetime

# ---------------- Logging Configuration ----------------
logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ---------------- Monitoring Function ----------------
def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    available_memory = memory.available / (1024 * 1024)  # Convert to MB

    return cpu_usage, memory_usage, available_memory


def log_metrics(cpu, memory, available_mem):
    logging.info(
        f"CPU Usage: {cpu}% | Memory Usage: {memory}% | Available Memory: {available_mem:.2f} MB"
    )


def display_metrics(cpu, memory, available_mem):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Available Memory: {available_mem:.2f} MB")
    print("-" * 50)


# ---------------- Main Loop ----------------
def main():
    print("Starting System Monitoring... Press Ctrl+C to stop.\n")
    try:
        while True:
            cpu, memory, available_mem = get_system_metrics()
            display_metrics(cpu, memory, available_mem)
            log_metrics(cpu, memory, available_mem)
            time.sleep(5)  # Collect data every 5 seconds

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        logging.info("System monitoring stopped manually.")


if __name__ == "__main__":
    main()
