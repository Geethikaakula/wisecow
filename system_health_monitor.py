
#!/usr/bin/env python3
import psutil, logging, time

logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
CPU_THRESHOLD, MEM_THRESHOLD, DISK_THRESHOLD = 80, 80, 80

def check_system_health():
    alerts = []
    if psutil.cpu_percent(interval=1) > CPU_THRESHOLD: alerts.append("High CPU usage")
    if psutil.virtual_memory().percent > MEM_THRESHOLD: alerts.append("High Memory usage")
    if psutil.disk_usage('/').percent > DISK_THRESHOLD: alerts.append("High Disk usage")
    if len(psutil.pids()) > 500: alerts.append("Too many processes")
    if alerts:
        for a in alerts: print("[ALERT]", a); logging.warning(a)
    else:
        print("System is healthy"); logging.info("System is healthy")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(60)
