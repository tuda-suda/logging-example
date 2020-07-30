import logging
import logging.config

# Вспомогательная функция, заггружает файл конфига в формате JSON
from utils import get_json_conf


def main():
    # Достаем объект логгера.
    # .getLogger() без аргументов возвращает логгер под именем "root"
    logger = logging.getLogger()
    logger.info('This is an INFO message on "root" logger')

    # Демонстрация различных уровней сообщений логгера
    logger.debug('I am DEBUG!')
    logger.info('I am INFO!')
    logger.warning('I am WARNING!')
    logger.error('I am ERROR!')
    logger.critical('I am CRITICAL!')

    # Демонстрация логирования с использованием исключений
    try:
        logger.warning('Here be dragons')
        raise Exception
    except Exception as e:
        logger.exception(f'Exception catched! {e}')

    # Тестовая библиотека, демонстрирующая работу логгера в нескольких файлах
    import mylib


if __name__ == "__main__":
    # Загружаем .conf конфиг
    logging.config.fileConfig('configs/logger.conf')

    # Загружаем JSON конфиг
    # Этот конфиг переопределит предыдущий
    log_config = get_json_conf()
    logging.config.dictConfig(log_config)

    # Заргузка конфига в виде python dict
    # Этот конфиг переопределит предыдущий
    from settings import LOGGING
    logging.config.dictConfig(LOGGING)

    main()