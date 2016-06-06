# autostager
Python port of [jumanjihouse's autostager](https://www.github.com/jumanjihouse/autostager)  
Stage a directory based on Github pull request (e.g., dynamic puppet environments)

###Install:
`pip install autostager`

###Usage:
```python
>>> from autostager import autostager
>>> autostager = autostager.Autostager() # creates a new autostager instance
>>> autostager.run()
```


