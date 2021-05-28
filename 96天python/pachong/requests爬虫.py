# import requests
# r = requests.get('https://api.github.com/events')
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# print(r)
import requests
r = requests.get('https://api.github.com/events')
print(r.text)

