import logging
import os
from logging import handlers
from common import CommonConfiguration  as cc

class Logger(object):
	level_relations = {
		'debug':logging.DEBUG,
		'info':logging.INFO,
		'warning':logging.WARNING,
		'error':logging.ERROR,
		'crit':logging.CRITICAL
	}

	def __init__(self,filename,level='info',when='D',backCount=3,
		fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
		self.logger = logging.getLogger(filename)
		format_str = logging.Formatter(fmt)
		self.logger.setLevel(self.level_relations.get(level))
		sh = logging.StreamHandler()
		sh.setFormatter(format_str)
		th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')
		th.setFormatter(format_str)
		self.logger.addHandler(sh)
		self.logger.addHandler(th)

if os.path.exists(cc.folderPath()):
	print('The folder has already existed')
else:
	os.makedirs(cc.folderPath())
log_path = cc.folderPath() + '/test.log'
log = Logger(log_path,level='info')
#log.logger.info('info message')