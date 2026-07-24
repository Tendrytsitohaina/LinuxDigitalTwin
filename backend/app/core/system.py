import platform
import datetime
import psutil
import os

def get_system_info():
    """
    Récupère les informations générales du système.
    Sources Linux :
    - /etc/os-release (distribution)
    - uname (noyau, hostname)
    - /proc/uptime (temps de fonctionnement)
    """
    # Distribution
    distro = "Unknown"
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    distro = line.split("=", 1)[1].strip().strip('"')
                    break
    except FileNotFoundError:
        distro = platform.system()  # Fallback

    # Temps de fonctionnement (uptime)
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = int((datetime.datetime.now() - boot_time).total_seconds())

    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "distribution": distro,
        "kernel_version": platform.release(),
        "architecture": platform.machine(),
        "uptime_seconds": uptime_seconds,
        "uptime_readable": str(datetime.timedelta(seconds=uptime_seconds)),
        # Source éducative : on indique où Linux stocke ces infos
        "_sources": {
            "distribution": "/etc/os-release",
            "hostname": "/proc/sys/kernel/hostname",
            "uptime": "/proc/uptime",
            "kernel": "uname -r"
        }
    }