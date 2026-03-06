import hashlib

class HashGenerator:
    """
    Clase para generar hashes de texto usando diversos algoritmos.
    """
    @staticmethod
    def generate(text, algorithm='sha512'):
        """
        Genera el hash de un texto usando el algoritmo especificado.
        Algoritmos comunes: 'md5', 'sha1', 'sha256', 'sha512'
        """
        try:
            # Convertir el texto a bytes
            text_bytes = text.encode('utf-8')
            
            # Crear el objeto hash
            hash_obj = hashlib.new(algorithm)
            
            # Actualizar con los bytes del texto
            hash_obj.update(text_bytes)
            
            # Obtener el hex digest
            return hash_obj.hexdigest()
        except ValueError:
            return f"Error: Algoritmo '{algorithm}' no soportado."

    @staticmethod
    def get_available_algorithms():
        """Retorna una lista de algoritmos disponibles."""
        return hashlib.algorithms_available
