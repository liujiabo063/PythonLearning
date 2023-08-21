import logging

logger = logging.getLogger(__name__)
import LoggingCase

if __name__ == '__main__':
    logger = LoggingCase.logs()

    logger.info("*************************数据处理分析报告*************************")
    logger.warning("操作不当可能导致错误发生")
    logger.debug("this is debug")
    logger.error("this is error")

