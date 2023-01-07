import utils
import read_csv
import charts
import pandas as pd


def run():
    """
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    result = utils.population_by_country(data, country)
    """
    df = pd.read_csv("./data.csv")
    df = df[df['Continent'] == 'Africa']

    countries = df['Country/Territory'].values
    print(countries)
    percentages = df['World Population Percentage'].values
    print(percentages)
    charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ')
    data = read_csv.read_csv('./data.csv')
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))
    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()
