sixgod pyton 网页正文提取
=====================================

思想
-------------------------
*  优势： 线性时间、不建DOM树、与HTML标签无关


```python
from vampire.htmlextract import HtmlExtract
import requests
html = requests.get('http://www.fabao365.com/fangchan/167193/')
html.encoding="utf-8"
ex = HtmlExtract()
print ex.get_text(html.text)
```
