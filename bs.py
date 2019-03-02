from bs4 import BeautifulSoup

with open("test.html") as inf:
	txt =inf.read()
	soup= BeautifulSoup(txt,'html.parser')
newline = soup.new_tag("h1", value="revanth")

h1= soup.find_all('h1')
soup.body.append(newline)
for tag in h1:
	tag.string.replace_with('Hey its came')

with open("test.html","w") as outf:
	outf.write(str(soup))