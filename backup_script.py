
#!/usr/bin/env python3
import os, subprocess, datetime, logging, sys

logging.basicConfig(filename="backup.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
SOURCE_DIR="/home/ubuntu/data"
REMOTE_USER="ubuntu"
REMOTE_HOST="192.168.1.100"
REMOTE_PATH="/home/ubuntu/backups"

def perform_backup():
    ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    f=f"backup_{ts}.tar.gz"
    try:
        subprocess.run(["tar","-czf",f,"-C",SOURCE_DIR,"."],check=True)
        subprocess.run(["scp",f,f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_PATH}"],check=True)
        logging.info(f"Backup successful: {f}"); print("[INFO] Backup successful:",f)
        os.remove(f)
    except subprocess.CalledProcessError as e:
        logging.error("Backup failed"); print("[ERROR] Backup failed:",e); sys.exit(1)

if __name__=="__main__":
    perform_backup()

