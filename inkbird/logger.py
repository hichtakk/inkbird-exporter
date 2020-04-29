from logging import getLogger, Formatter, StreamHandler, INFO

logger = getLogger(__name__)
logger.setLevel(INFO)
handler = StreamHandler()
handler.setLevel(INFO)
formatter = Formatter("%(levelname)s : %(asctime)s : %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)