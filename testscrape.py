import requests
from bs4 import BeautifulSoup


result = requests.get('https://www.rappler.com/technology')
print (result)

res_content = result.content

parsed_res = BeautifulSoup(res_content)

print(parsed_res)

# test_file = open('test.txt', 'a')
# test_file.write(parsed_res)