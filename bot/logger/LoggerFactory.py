import logging
from datetime import datetime


class LoggerFactory:

    @staticmethod
    def getLogger(name, log_path="./logs", logging_level=logging.INFO) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging_level)

        current_date = datetime.now().strftime("%Y-%m-%d")
        handler = logging.FileHandler(f"{log_path}/log_{current_date}.txt")

        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
