import logging
import datetime
import traceback


class DBHandler(logging.Handler):
    def emit(self, record):
        try:
            from world.models import SystemErrorLog
            text = record.exc_text
            if text is None:
                if record.exc_info and len(record.exc_info) > 1:
                    text = ''.join(traceback.format_exception(*record.exc_info))
            logEntry = SystemErrorLog(level=record.levelname, message=text, timestamp=datetime.datetime.now())
            logEntry.save()
        except Exception  as e:
            pass