import logging

logging.basicConfig(

    filename=
    "logs/application.log",

    level=logging.INFO,

    format=
    "%(asctime)s - %(message)s"
)

logger = logging.getLogger()