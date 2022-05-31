favorate_languages = {
    'A': 'english',
    'C': 'chinese',
    'D': 'python',
    'X': 'ahahha',
}
inquiry_list = ['A', 'C', 'D', 'W','X','H','M']
for name in inquiry_list:
    if name in favorate_languages.keys():
        print('Thank '+name+' you for participating in the survey')
    else:
        print('I invite  '+name+' to participate in the survey')
