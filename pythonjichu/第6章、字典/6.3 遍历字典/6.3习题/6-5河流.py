rivers = {
    'Rhine': 'Switzerland',
    'changJiang': 'china',
    'nile': 'egypt',
}
for river, country in rivers.items():
    print('The ' + river.title() + 'runs through the ' + country.title() + '.')##items 用法
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())



