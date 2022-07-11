from django.core.exceptions import ValidationError
import pint

# valid_unit_measurement = ['pounds', 'lbs', 'oz', 'gram']


# def validate_unit_of_mesure(value):
#     if value not in valid_unit_measurement:
#         raise ValidationError(f'{value} is not a valid unit of measurement')


def validate_unit_of_mesure(value):
    Ureg = pint.UnitRegistry()
    try:
        single_unit = Ureg[value]
    except:
        raise ValidationError(f'{value} is not a valid unit of measurement')
