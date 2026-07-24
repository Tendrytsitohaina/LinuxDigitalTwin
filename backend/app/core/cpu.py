import psutil

def get_cpu_info():
    """
    Récupère les informations du CPU.
    Sources Linux :
    - /proc/cpuinfo (modèle, coeurs physiques)
    - /sys/devices/system/cpu/ (coeurs logiques)
    - /proc/stat (utilisation)
    """
    cpu_freq = psutil.cpu_freq()
    
    # Calcul du pourcentage d'utilisation par coeur
    per_cpu_percent = psutil.cpu_percent(interval=0.5, percpu=True)
    global_percent = psutil.cpu_percent(interval=0.5)

    return {
        "model": "Unknown",
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "max_frequency_mhz": round(cpu_freq.max, 2) if cpu_freq else None,
        "current_frequency_mhz": round(cpu_freq.current, 2) if cpu_freq else None,
        "global_usage_percent": global_percent,
        "per_core_usage_percent": per_cpu_percent,
        "_sources": {
            "model_physical": "/proc/cpuinfo (model name, cpu cores)",
            "logical_cores": "/sys/devices/system/cpu/present",
            "frequency": "/sys/devices/system/cpu/cpu0/cpufreq/",
            "usage": "/proc/stat"
        }
    }