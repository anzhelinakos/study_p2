import psutil
import datetime

def show_boottime_info():
    boottime = psutil.boot_time()
    info = datetime.datetime.fromtimestamp(boottime).strftime("%Y-%m-%d %H:%M:%S")
    boottime_info = f"\nLast boot of this PC was {info}\n"
    print(boottime_info)


def show_cputime_info(cputime_info):
    cputime_info_edit = (f"Current values of system CPU times for:\n   "
                         f"-user is {cputime_info['user']} s; \n   "
                         f"-nice is {cputime_info['nice']} s; \n   "
                         f"-system is {cputime_info['system']} s; \n   "
                         f"-idle is {cputime_info['idle']} s.\n")
    print(cputime_info_edit)


def show_cpupercent_info(cpupercent_info):
    cpupercent_info_edit = f"CPU utilization is {cpupercent_info} %\n"
    print(cpupercent_info_edit)


def show_cpucount_info(cpucount_info):
    cpucount_info_edit = f"Number of logical CPUs is {cpucount_info}\n"
    print(cpucount_info_edit)


def show_cpufreq_info(cpufreq_info):
    cpufreq_info_edit = f"Min CPU frequency = {cpufreq_info.min}, Max CPU frequency = {cpufreq_info.max}\n"
    print(cpufreq_info_edit)


def show_virtualmemory_info(virtualmemory_info):
    virtualmemory_info_edit = (f"System memory usage:\n    "
                               f"-total: {round(virtualmemory_info.total/(2**30),3)} Gb\n    "
                               f"-available: {round(virtualmemory_info.available/(2**30),3)} Gb\n    "
                               f"-used: {round(virtualmemory_info.used/(2**30),3)} Gb\n    "
                               f"-free: {round(virtualmemory_info.free/(2**30),3)} Gb\n    "
                               f"-active: {round(virtualmemory_info.active/(2**30),3)} Gb\n    "
                               f"-inactive: {round(virtualmemory_info.inactive/(2**30),3)} Gb\n")
    print(virtualmemory_info_edit)


def show_netiocounters_info(netinfocounters_info):
    netinfocounters_info_edit = (f"Network statistic is:\n   "
                                 f"- sent  {round(netinfocounters_info.bytes_sent/(2**30),3)} Gb\n   "
                                 f"- recived {round(netinfocounters_info.bytes_recv/(2**30),3)} Gb\n")
    print(netinfocounters_info_edit)


def show_processes_info():
    print("Processes information:")
    for proc in psutil.process_iter():
        process_info = f"pid={proc.pid}, Name of process is  {proc.name()},   Current status: {proc.status()}"
        print(process_info)
    return
