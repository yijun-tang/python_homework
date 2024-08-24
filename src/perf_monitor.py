import time
import functools
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def performance_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log function name and arguments
        logger.info(
            f"Function '{func.__name__}' called with arguments {args} and keyword arguments {kwargs}"
        )

        # Record start time
        start_time = time.time()

        # Execute the function
        result = func(*args, **kwargs)

        # Calculate execution time
        end_time = time.time()
        execution_time = end_time - start_time

        # Log execution time
        logger.info(
            f"Function '{func.__name__}' executed in {execution_time:.4f} seconds"
        )

        return result

    return wrapper
