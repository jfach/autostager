from distutils.core import setup
setup(
  name = 'autostager',
  packages = ['autostager'],
  version = '0.1.23',
  description = 'Stage a directory based on Github pull request (e.g., dynamic puppet environments)',
  author = 'Jordan Facibene',
  author_email = 'jordan.facibene13@stjohns.edu',
  url = 'https://github.com/jfach/autostager',
  download_url = 'https://github.com/jfach/autostager/tarball/0.1.23',
  keywords = ['github', 'automation', 'staging'],
  classifiers = [],
  install_requires = ['github3.py']
)

