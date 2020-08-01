LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "verbose",
            "filename": "py-dict.log"
        }
    },
    "formatters": {
        "simple": {
            "class": "logging.Formatter",
            "style": "{",
            "format": "{name} - [{levelname}]: {message}"
        },
        "verbose": {
            "class": "logging.Formatter",
            "style": "{",
            "format": "{asctime} - {name} - [{levelname}]: line {lineno} - {message}",
            "datefmt": "%I:%M:%S"
        }
    },
    "loggers": {
        "mylib": {
            "handlers": ["consoleHandler", "fileHandler"],
            "level": "INFO",
            "propagate": False
        }
    },
    "root": {
        "handlers": ["consoleHandler"],
        "level": "DEBUG"
    }
}