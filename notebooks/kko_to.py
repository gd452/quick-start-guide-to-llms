import requests

def shorten_url(long_url):
    url = 'https://kko.to/v2/create'
    headers = {
        'Content-Type': 'application/json',
        # 필요시 여기에 추가 헤더를 넣습니다.
    }
    data = {
        # 필요시 여기에 추가 폼 데이터를 넣습니다.
        'url': 'https://www.google.com',
        'by': 'gd.re'
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    if response.status_code == 200:
        return response.json().get('url')
    else:
        return None

if __name__ == "__main__":
    import sys
    long_url = sys.argv[1]
    short_url = shorten_url(long_url)
    if short_url:
        print(short_url)
    else:
        print("Error shortening URL")

