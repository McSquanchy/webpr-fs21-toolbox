from bs4 import BeautifulSoup
import pypandoc

output = pypandoc.convert_file(
    'toolbox.md', 'html', outputfile='docs\index.html',
    extra_args=["-s", "-c", "css/mvp.css",
                "--template=template.html", "--toc", "--toc-depth=2"])


with open("docs\index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for a in soup.find_all('a', href=True):
    if "http" in a['href']:
        a['target'] = "_blank"

with open("docs\index.html", "w", encoding='utf-8') as file:
    file.write(str(soup))
