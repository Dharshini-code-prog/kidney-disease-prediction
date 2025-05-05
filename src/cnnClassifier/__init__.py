import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 
# %(asctime)s  → Timestamp of when the log was recorded (e.g., 2025-05-04 10:30:00)
# %(levelname)s → The severity level of the log (e.g., INFO, WARNING, ERROR)
# %(module)s   → The name of the Python module (file) where the log was triggered
# %(message)s  → The actual log message provided by the developer
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") # this ill store all logs files
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),# Write log messages to the log file
         # Also print log messages to the console
        logging.StreamHandler(sys.stdout)
    ]
)
# Create a custom logger instance with the name "cnnClassifierLogger"
logger = logging.getLogger("cnnClassifierLogger")