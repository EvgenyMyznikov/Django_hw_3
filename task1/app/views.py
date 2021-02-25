import csv
from django.shortcuts import render


def inflation_view(request):
	template_name = 'inflation.html'
	data = []
	with open('inflation_russia.csv', newline='') as csv_file:
		file = csv.DictReader(csv_file, delimiter=";")
		for row in file:
			row = {'Год': row['Год'], 'Янв': row['Янв'], 'Фев': row['Фев'], 'Мар': row['Мар'], 'Апр': row['Апр'],
				   'Май': row['Май'], 'Июн': row['Июн'], 'Июл': row['Июл'], 'Авг': row['Авг'], 'Сен': row['Сен'],
				   'Окт': row['Окт'], 'Ноя': row['Ноя'], 'Дек': row['Дек'], 'Суммарная': row['Суммарная']}
			headers = row.keys()
			for key, value in row.items():
				if value == '':
					row.update({key: '-'})
			data.append(row)

	context = {'inflation_data': data, 'headers': headers}
	return render(request, template_name, context)
