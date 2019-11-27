template_img = """
<a href="{link}">
    <img src="{src}" />
</a>
"""

template_pdf = """
<a href="{link}">
    <object data="{src}" type="application/pdf"
            width="100%" height="100%">
    </object>
</a>
"""


from glob import glob
import random

files = glob('logos/*.jpg') + \
        glob('logos/*.pdf') + \
        glob('logos/*.png')
random.shuffle(files)

T = ''

for f in files:
    if f.endswith('.jpg') or f.endswith('.png'):
        t = template_img.format(link=f, src=f)
    elif f.endswith('.pdf'):
        t = template_pdf.format(link=f, src=f)
    T += t
    # print(t)

with open('index.html.template') as fin:
    temp = fin.read()
    out = temp.replace('{{ logolist }}', T)
    with open('index.html', 'w') as fout:
        fout.write(out)

