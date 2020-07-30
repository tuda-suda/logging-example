import logging


logger = logging.getLogger(__name__)
logger.info("Logging from mylib!")


from .a import func_a
from .b import func_b

func_a()
func_b()