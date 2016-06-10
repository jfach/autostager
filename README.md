# autostager
Python port of [jumanjihouse's autostager](https://www.github.com/jumanjihouse/autostager)  
Stage a directory based on Github pull request (e.g., dynamic puppet environments)

###Install:
`pip install autostager`

###Setup:
Export environment variables:  
`access_token` *40 character Github access token*  
`repo_slug` *repository that you want to track*  
`base_dir` *directory to stage PRs in*  
```
>>> export access_token=<your 40-char token>
>>> export repo_slug=jfach/autostager
>>> export base_dir=/path/to/base/dir
```

###Usage:
```python
>>> from autostager import autostager
>>> autostager = autostager.Autostager() # creates a new autostager instance
>>> autostager.run()
```


