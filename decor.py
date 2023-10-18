import datetime
import json

def log(file_name):
    def record_info(func):
        info_string = "{0} ({1})\n"
        def record_info_worker(*args, **kwargs):
            res = func()
            with open(file_name, "a") as info_record_file:
                info_record_file.write(json.dumps(info_string.format(datetime.datetime.now(), res)))
            return res
        return record_info_worker
    return record_info

def speed_info(func):
    file_name = "speed_info.log"
    info_string = "{0} ({1})\n"

    def speed_info_worker(*args, **kwargs):
        start = datetime.datetime.now()
        res = func()
        res1 = datetime.datetime.now() - start
        with open(file_name, "a") as speed_info_file:
            speed_info_file.write(info_string.format(func.__name__, res1))
        return res
    return speed_info_worker