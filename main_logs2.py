# import logging
# import traceback

# # try:
# #     a = [1, 2, 3]
# #     val = a[4]
# # except IndexError as e:
# #     logging.error(e, exc_info=True)

# try:
#     a = [1, 2, 3]
#     val = a[4]
# except:
#     logging.error("The error is %s", traceback.format_exc())

#----------------------------------

# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('Hello, world!')

# ----------------------------------

import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)



