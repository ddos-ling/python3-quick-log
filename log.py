import logging
import os
from logging.handlers import TimedRotatingFileHandler
import colorlog

log_colors_config = {
    'DEBUG': 'blue',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

class log:
    def __init__(self,module_name,level=logging.INFO):
        # 初始化日志系统
        self.module_name = module_name
        self.prefix = f"{module_name} - "

        if not "log" in os.listdir("./"):
            os.mkdir("log")
        if not module_name in os.listdir("./log"):
            os.mkdir(f"log/{module_name}")
        LOG_FORMAT = logging.Formatter("%(asctime)s %(threadName)s(%(thread)d) [%(levelname)s] %(message)s")
        # logging.basicConfig(filename=f"log/{module_name}/{t.getStrDate()}.log",level=logging.DEBUG,format=LOG_FORMAT,encoding="utf-8")
        self.logg = logging.getLogger(module_name)
        self.logg_c = logging.StreamHandler()
        self.logg.setLevel(level)
        self.logg_c.setLevel(level)

        # 文件输出
        file_log = TimedRotatingFileHandler(filename=f"log/{module_name}/{module_name}.log", when='D', interval=1, backupCount=30,encoding="utf-8")
        file_log.setLevel(level)
        file_log.setFormatter(LOG_FORMAT)
        self.logg.addHandler(file_log)

        console_log = colorlog.ColoredFormatter(
            fmt='%(log_color)s%(asctime)s %(threadName)s(%(thread)d) [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=log_colors_config
        )
        self.logg_c.setFormatter(console_log)
        self.logg.addHandler(self.logg_c)
        self.logg_c.close()

        self.info(f"日志初始化完成")

    def info(self,message):
        self.logg.info(self.prefix + str(message))

    def debug(self,message):
        self.logg.debug(self.prefix + str(message))

    def warning(self,message):
        self.logg.warning(self.prefix + str(message))

    def error(self,message):
        self.logg.error(self.prefix + str(message))

    def critical(self,message):
        self.logg.critical(self.prefix + str(message))