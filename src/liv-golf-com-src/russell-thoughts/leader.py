import requests

url = "https://www.livgolf.com/leaderboard"

payload = "[{\"season\":2022}]"
headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Next-Action': '71b232f32aa5c7eddc5d7505ffbd8735adfc5f7a',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22pageName%22%2C%22leaderboard%22%2C%22oc%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fleaderboard%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Accept': 'text/x-component',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'host': 'www.livgolf.com'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
