from distutils.core import setup


kw = dict(name='vampire',
          version='0.0.2',
          py_modules=['vampire','vampire/utils'],
          author="intoblack",
          author_email="intoblack86@gmail.com",
          description="html content extract",
          keywords="html cotent extract",
          url='https://github.com/intoblack/sixgod',
          download_url='https://github.com/intoblack/sixgod',
          packages=['vampire','vampire/utils'])


setup(**kw)
