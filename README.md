# autostager
Python port of [jumanjihouse's autostager](https://www.github.com/jumanjihouse/autostager)  
Stage a directory based on Github pull request (e.g., dynamic puppet environments)


###Install:
`pip install autostager`

###Setup:
Create a Github access_token and export a few environment variables:
```
>>> export repo_slug=jfach/testrepo
>>> export access_token=<your 40-char token>
>>> export base_dir=/path/to/base/dir
```

###Usage:
```python
>>> from autostager import autostager
>>> autostager = autostager.Autostager() # creates a new autostager instance
>>> autostager.run()
```


