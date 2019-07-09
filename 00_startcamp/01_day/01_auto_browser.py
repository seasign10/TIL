# import webbrowser
# browser = ['www.google.com', 'www.naver.com', 'www.daum.net']
# for a in browser:
    # webbrowser.open_new(a)

# idols = ['bts', 'hot', 'BoA', 'ss501']
# url = 'https://search.naver.com/search.naver?query='

# for idol in idols:
#     webbrowser.open_new(url + idol)

import requests

response = requests.get('https://www.naver.com/').status_code
print(response)
