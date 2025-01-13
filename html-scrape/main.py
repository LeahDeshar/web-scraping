from bs4 import BeautifulSoup


with open('index.html', 'r') as fp:
    content = fp.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h5')
    for course in tags:
        print(course.text)