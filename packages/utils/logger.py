from loguru import logger
from pathlib import PurePath
import sys


class Logger:
    __config = {
        'backtrace': True,
        'diagnose': True,
        'format': '{time} [{level}] {message}'
    }
    debug = logger.debug
    info = logger.info
    warning = logger.warning
    error = logger.error
    exception = logger.opt(exception=True).critical

    @staticmethod
    def config(config=None):
        if not config:
            return
        console = config.get('console')
        file = config.get('file', dict())
        if console:
            logger.remove()
            console_config = Logger.__config.copy()
            _format = console.get('format')
            if _format:
                console_config['format'] = _format
            console_config['colorize'] = True
            logger.add(sys.stdout, **console_config, level='DEBUG')
        if file:
            path = file.get('path')
            if not path:
                return
            console_config = Logger.__config.copy()
            _format = file.get('format')
            if _format:
                console_config['format'] = _format
            console_config['rotation'] = file.get('rotation')
            logger.add(
                PurePath(path, 'app.log'),
                **console_config,
                filter=lambda record: record['level'].name in ['DEBUG', 'INFO', 'WARNING']
            )
            logger.add(
                PurePath(path, 'error.log'),
                **console_config,
                filter=lambda record: record['level'].name in ['ERROR', 'CRITICAL']
            )

