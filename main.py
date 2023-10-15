from get_func import (get_cpupercent_info, get_cputime_info,
                      get_cpucount_info, get_cpufreq_info,
                      get_virtualmemory_info, get_netiocounters_info)
from show_func import (show_cpufreq_info, show_netiocounters_info,
                       show_virtualmemory_info, show_cputime_info,
                       show_boottime_info, show_cpucount_info,
                       show_cpupercent_info, show_processes_info)
from pathlib import Path
def main():
    cputime_info = get_cputime_info()
    cpupercent_info = get_cpupercent_info()
    cpucount_info = get_cpucount_info()
    cpufreq_info = get_cpufreq_info()
    virtualmemory_info = get_virtualmemory_info()
    netinfocounters_info = get_netiocounters_info()
    show_boottime = show_boottime_info()
    show_cputime = show_cputime_info(cputime_info)
    show_cpupercent = show_cpupercent_info(cpupercent_info)
    show_cpucount = show_cpucount_info(cpucount_info)
    show_cpufreq = show_cpufreq_info(cpufreq_info)
    show_virtualmemory = show_virtualmemory_info(virtualmemory_info)
    show_netiocounters = show_netiocounters_info(netinfocounters_info)
    show_processes = show_processes_info()


file_name = "main.py"
path_to_file = Path(__file__)
project_dir = path_to_file.parent
full_path = project_dir / file_name
print(f"Path to main file is:\n", full_path)


if __name__ == '__main__':
    main()
