from django import template

register = template.Library()


@register.filter()
def colors(value: str) -> str:
	try:
		value = float(value)
		if value < 0:
			color = 'darkgreen'
		elif value <= 0.99:
			color = 'white'
		elif 1 <= value < 1.99:
			color = 'Pink'
		elif 2 <= value < 4.99:
			color = 'LightCoral'
		elif value >= 5:
			color = 'red'
		else:
			color = ''
	except ValueError:
		color = ''
	return color

