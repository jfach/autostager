import os
from subprocess import Popen, PIPE
import logger

class PullRequest():

    def __init__(self,
                 branch,
                 clone_url,
                 base_dir,
                 name,
                 upstream):
        self.branch = branch
        self.clone_url = clone_url
        self.base_dir = base_dir
        self.name = name
        self.upstream_url = upstream
        self.staging_dir = os.path.join(self.base_dir, self.name)

    def local_sha(self):
        os.chdir(self.staging_dir)
        args = ["git", "log", "--pretty='%H'", "HEAD^1.."]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        return output

    def staged(self):
        return os.path.isfile(self.staging_dir)

    def behind(self, treeish):
        os.chdir(self.staging_dir)
        args = ["git", "log", "--oneline", "..{0}".format(treeish)]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        return len(output.split('\n'))

    # A threshold for how many commits a branch can be behind upstream.
    # this should be a variable instead?
    def behind_threshold(self):
        return 10

    def up2date(self, treeish):
        return self.behind(treeish) <= self.behind_threshold()

    def rebase(self): #???
        logger.log("rebase origin/{0}".format(self.branch))
        os.chdir(self.staging_dir)
        args = ["git", "rebase", "origin/{0}".format(self.branch), "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        status = cmd.returncode
        self.update_submodules()
        logger.log("{0} is at revision {1}".format(self.branch, self.local_sha()))
        return status

    def reset_hard(self):
        os.chdir(self.staging_dir)
        args = ["git", "reset", "--hard", "origin/{0}".format(self.branch), "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        self.update_submodules()

    def fetch(self):
        logger.log("git fetch")
        os.chdir(self.staging_dir)
        self.add_upstream_remote()
        args = ["git", "fetch", "--all", "--prune", "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        pass

    def update_submodules(self):
        logger.log("update submodules in {0}".format(self.staging_dir))
        args = ["git", "submodule", "sync", "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        args = ["git", "submodule", "update", "--init", "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        pass
        
    def remote(self, s): # what is s ???
        os.chdir(self.staging_dir)
        args = ["git", "remote", "-v"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        remotes = output.split('\n')
        if remotes[-1] == '':
            remotes = remotes[:-1]
        urls = []
        for remote in remotes:
            remote = remote.split("\t")[-1].split(' ')[0]
            if remote not in urls:
                urls.append(remote)
        return s in urls

    def add_upstream_remote(self):
        os.chdir(self.staging_dir)
        logger.log("add upstream remote")
        args = ["git", "remote", "add", "upstream", self.upstream_url, "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        args = ["git", "fetch", "--prune", "upstream", "&>" "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        pass

    def clone(self):
        logger.log("clone to {0}".format(self.staging_dir))
        if not os.path.exists(self.base_dir):
            os.path.makedirs(self.base_dir)
        args = ["git", "clone", "-b", self.base_dir, self.clone_url, self.staging_dir, "&>", "/dev/null"]
        cmd = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = cmd.communicate()
        os.chdir(self.staging_dir)
        self.add_upstream_remote()
        self.update_submodules()
        pass

