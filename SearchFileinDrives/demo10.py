
import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Set the logging level to DEBUG (or any other level you prefer)
logger.setLevel(logging.DEBUG)

# Create a file handler to write logs to a file
file_handler = logging.FileHandler('my_project.log')

# Create a formatter to specify the format of the logs
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger object
logger.addHandler(file_handler)

# Now you can use the logger object to log messages
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')


