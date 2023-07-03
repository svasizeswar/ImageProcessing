
url_list = [
  {
    "Status": "Webpage is accessible",
    "URL": "https://www.metro.net/about/careers/"
  },
  {
    "Status": 404,
    "URL": "https://www.metro.net/moredtla/sds"
  },
  {
    "Status": 404,
    "URL": "https://www.metro.net/riding/guide/sds"
  },
  {
    "Status": "Webpage is accessible",
    "URL": "https://www.metro.net/about/"
  }
]

url = sorted(url_list, key=lambda x: x['Status'] == 'Webpage is accessible')

print (url)
