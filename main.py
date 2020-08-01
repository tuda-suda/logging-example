import logging
import logging.config

# Вспомогательная функция, загружает файл конфига в формате JSON
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
        # Если нужно после логирования остановить работу программы,
        # то можно заново выбросить исключение:
        # raise e

    # Тестовая библиотека, демонстрирующая работу логгера в нескольких файлах.
    # Здесь выполняется логика в mylib/__init__.py
    import mylib


if __name__ == "__main__":
    # Загрузка конфигов


    # Конфиги можно устанавливать через метод .basicConfig(), через метод .dictConfig() из словаря python,
    # либо загружать из файла конфига формата .conf.
    # Также с помощью .dictConfig() можно загружать из любых форматов, которые можно преобразовать 
    # в словарь python: JSON, yaml и т.д.

    # Загружаем .conf конфиг
    logging.config.fileConfig('configs/logger.conf')

    # Загружаем JSON конфиг
    # Этот конфиг переопределит предыдущий
    logging.config.dictConfig(get_json_conf())

    # Заргузка конфига в виде python dict
    # Этот конфиг переопределит предыдущий
    from configs.settings import LOGGING
    logging.config.dictConfig(LOGGING)

    main()