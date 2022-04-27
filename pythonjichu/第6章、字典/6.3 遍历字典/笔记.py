# 6.3.1 遍历所有的键 遍 —值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for k,v in user_0.items():
    print("\nKey: " + k)
    print("\nKey: " + v)

favorite_languages = { 'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python',
                       }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "
          + language.title()
          + ".")
# 6.3.2 遍历字典中的所有键
favorite_languages = { 'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python',
                       }
for k in favorite_languages.keys():
    print(k.title())
for k in favorite_languages:
    print(k.title())
favorite_languages = { 'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python',
                       }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
if name in friends:
    print(" Hi " + name.title() + ", I see your favorite language is " +favorite_languages[name].title() + "!")


