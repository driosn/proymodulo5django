from django.core.exceptions import ValidationError

def contiene_numero(string):
    return any(char.isdigit() for char in string)

def validar_nombre(value):
    if contiene_numero(value):
        raise ValidationError(
            '%(value)s no es un nombre valido',
            params={'value': value}
        )

def validar_calificacion(value):
    if value < 0 | value > 100:
        raise ValidationError(
            '%(value)s no es una calificacion valida',
            params={'value': value}
        )