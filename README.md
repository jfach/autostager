#autostager     
        ___    __  __ ______ ____  _____ ______ ___    ______ ______ ____
       /   |  / / / //_  __// __ \/ ___//_  __//   |  / ____// ____// _ _ \
      / /| | / / / /  / /  / / / /\__ \  / /  / /| | / / __ / __/  / /_/ /
     / ___ |/ /_/ /  / /  / /_/ /___/ / / /  / ___ |/ /_/ // /___ / _, _/
    /_/  |_|\____/  /_/   \____//____/ /_/  /_/  |_|\____//_____//_/ |_|
    
Python port of [jumanjihouse's autostager](https://www.github.com/jumanjihouse/autostager)  
Stage a directory based on Github pull request (e.g., dynamic puppet environments)

###Install:
Clone the repo: `git clone https://github.com/jfach/autostager.git`   
**OR**  
Install via pip: `pip install autostager`

###Setup:
Export environment variables:  
`access_token` *40 character Github access token*  
`repo_slug` *repository that you want to track*  
`base_dir` *directory to stage PRs in*  
`timeout` *timeout seconds for git operations, default is 120*

- You can generate a token from the command line by running the following script: https://gist.github.com/Jfach/ec85c6550cf9fc99e3a708bd45ec6a8c  
- Make sure to give the token the necessary access privileges.   
- This can be done by going to Settings > Personal Access Tokens > Edit
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


