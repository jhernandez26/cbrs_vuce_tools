import logging
import os
from logging.handlers import RotatingFileHandler

class CustomLogger:
    """
    Clase para gestionar el guardado de logs con soporte para rotación automática.
    """
    def __init__(self, app_name, log_path, log_level=logging.INFO, max_size_gb=1, backup_count=3):
        """
        Inicializa el logger.
        
        :param app_name: Nombre de la aplicación (usado para el nombre del archivo .log).
        :param log_path: Directorio donde se guardará el log.
        :param log_level: Nivel de log inicial (por defecto logging.INFO).
        :param max_size_gb: Tamaño máximo del archivo antes de rotar en GIGABYTES (por defecto 1GB).
        :param backup_count: Número de archivos de respaldo a mantener (por defecto 3).
        """
        self.app_name = app_name
        self.log_path = log_path
        self.log_level = log_level
        self.max_bytes = max_size_gb * 1024 * 1024 * 1024  # Conversión de GB a Bytes
        self.backup_count = backup_count
        
        # Asegurarse de que el directorio del log existe
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)
            
        # Formar el nombre completo del archivo de log
        self.log_filename = os.path.join(self.log_path, f"{self.app_name}.log")
        
        # Configurar el logger
        self.logger = logging.getLogger(self.app_name)
        self.logger.setLevel(self.log_level)
        
        # Evitar duplicados si se llama varias veces para el mismo logger
        if not self.logger.handlers:
            # Crear el manejador con rotación automática
            handler = RotatingFileHandler(
                self.log_filename, 
                maxBytes=self.max_bytes, 
                backupCount=self.backup_count,
                encoding='utf-8'
            )
            
            # Definir el formato del log
            # Formato: [Fecha Hora] [Nivel] [Clase/Módulo] - Mensaje
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            handler.setFormatter(formatter)
            
            # Asociar el manejador al logger
            self.logger.addHandler(handler)

    def debug(self, message):
        """Log level DEBUG - Para información detallada."""
        self.logger.debug(message)

    def info(self, message):
        """Log level INFO - Para eventos generales de la aplicación."""
        self.logger.info(message)

    def warning(self, message):
        """Log level WARNING - Para situaciones que requieren atención pero no son críticas."""
        self.logger.warning(message)

    def error(self, message):
        """Log level ERROR - Para errores que afectan el funcionamiento de algo específico."""
        self.logger.error(message)

    def critical(self, message):
        """Log level CRITICAL - Para fallos graves del sistema."""
        self.logger.critical(message)

    def log_header(self, title=None):
        """
        Escribe una cabecera decorativa en el log para marcar inicios de proceso o secciones.
        """
        app_title = title if title else self.app_name
        separator = "=" * 30
        header_text = f"{separator} [ {app_title.upper()} ] {separator}"
        self.logger.info(f"\n{header_text}")

