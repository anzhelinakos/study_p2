import psutil
import datetime
from decor import record_info
from decor import speed_info

@record_info
def get_cputime_info():
    return {"user": psutil.cpu_times().user,
            "nice": psutil.cpu_times().nice,
            "system": psutil.cpu_times().system,
            "idle": psutil.cpu_times().idle}


@record_info
@speed_info
def get_cpupercent_info():
    return psutil.cpu_percent()


@record_info
@speed_info
def get_cpucount_info():
    return psutil.cpu_count()


@record_info
def get_cpufreq_info():
    return psutil.cpu_freq()


@record_info
def get_virtualmemory_info():
    return psutil.virtual_memory()


def get_netiocounters_info():
    return psutil.net_io_counters()

