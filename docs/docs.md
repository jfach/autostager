Intro: 
--------

Autostager contributes to projects by forking and cloning Pull Request. It performs an automatic staging operation on new or existing fork from Github's Pull Request. Instead of cloning the fork's data manually from Github, Autostager will draw fork's data from Github and stage in base directory at local machine. It also allows maintainer to test branch/es and  merge branch/es.  
Imagine you are collobrating with 80 contributors to a project, Autostager stagesall forks and branches for the maintainer automaticly stages directory from PRs

Autostager uses for automaticly staging new or existing fork from Github's Pull Request<br>

Purpose:
--------

Autostager to pull all forks and from the fork branches from <repo> to local machine.<br>

How:<br>
--------
#####include function from autostager.py
1. call out to github APl (Pull Request)<br>
2. for each pull request clone each fork and its branch <br>
3. stage each fork and it's branch in to a directory<br>
⋅⋅ if the fork is already staged(exist) <br>
⋅⋅ -> fetch and rebase the fork <br>
⋅⋅ else<br>
⋅⋅ -> repeat step 2<br>
*Step3 acts as loop to look for new and existing fork<br> 

Procedure:<br>
---------
#####For Maintainer
Follow (procedure) [ https://help.github.com/articles/creating-an-access-token-for-command-line-use/] to generate token forcommand line use
```
export access_token=<your_token>
export repo_slug=<path of repo in github>
export base_dir=<Directory Pull Request get stage>
```
#####For contributor:
```	
git remote add <url of maintainer's repo><br>
git remote -v <br>
``` 	

example:
```
	gary@gary-HP-2000-Notebook-PC:~/Desktop/testrepo$ git remote -v 
	origin	https://github.com/Garysoccer/testrepo.git (fetch) #contributor
	origin	https://github.com/Garysoccer/testrepo.git (push)
	upstream  https://github.com/jfach/testrepo.git (fetch) #maintainer	
	upstream  https://github.com/jfach/testrepo.git (push)

```
Sync fork with Maintainer' Branch 
----------
Ensure github3 version is 0.9.3
```
pip install --pre github3.py

Sync fork with Maintainer' Branch 
----------
```
$git fetch upstream
$git checkout <master>
$git rebase upstream/master
$git checkout <branch>
$git rebase <master>
$git add <file>
$git commit -m "..."
$git push --force
$git fetch upstream


what does autostager do : stges data from Pull request.
```
$git checkout <master>
$git push

>>>>>>> origin/production



