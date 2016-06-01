import os
import shutil
import github3
import logger
import pull_request

class Autostager():

    def __init__(self):
        slug = self.repo_slug().split('/')
        self.owner = slug[0]
        self.repo = slug[1]
        self.access_token = os.environ.get('access_token')

    def access_token(self):
        return os.environ['access_token']

    def alphafy(self, a_string):
        pass

    def stage_upstream(self):
        default_branch = client.repository(self.owner, self.repo).default_branch
        logger.log("===> begin {0}".format(default_branch))
        p = pull_request.PullRequest(
            default_branch,
            self.authenticated_url("https://github.com/{0}".format(self.repo_slug())),
            self.base_dir(),
            default_branch,
            self.authenticated_url("https://github.com/{0}".format(self.repo_slug()))
        )
        if not p.staged():
            p.clone()
        p.fetch()
        if p.rebase():
            return
        self.client.repository(self.owner, self.repo).create_issue(
            "Failed to fast-forward {0} branch".format(default_branch),
            ":bangbang: This probably means somebody force-pushed to the branch."
        )
        pass



    def process_pull(self, pr):
        logger.log("===> {0} {1}".format(pr.number, self.staging_dir(pr)))


    def comment_or_close(self, p, pr, add_comment = True):
        pass


    def authenticated_url(self, s):
        pass


    def base_dir(self):
        return os.environ.get('base_dir') or '/opt/puppet/environments'


    def clone_dir(self, pr):
        alphafy(pr.head.label)


    def staging_dir(self, pr):
        os.path.join(self.base_dir(), self.clone_dir(pr))


    def repo_slug(self):
        return os.environ.get('repo_slug') # handle None return value if key does not exist?


    def client(self):
        return github3.login(token=access_token())


    def timeout_seconds(self):
        result = 120
        if os.environ.get('timeout'):
            result = int(os.environ['timeout'])
            assert result > 0, "timeout must be greater than zero seconds"
        return result


    def safe_dirs(self):
        return ['.', '..', 'production']

    def run(self):
        self.client()
        self.stage_upstream()
        prs = client.repository(self.owner, self.repo).pull_requests()
        new_clones = [self.clone_dir(pr) for pr in prs]
        if os.path.exists(self.base_dir()):
            discard_dirs = set(os.listdir(self.base_dir())) - set(self.safe_dirs()) - set(new_clones)
            discard_dirs = list(discard_dirs)
            discard_dirs = [os.path.join(self.base_dir(), d) for d in discard_dirs]
            for discard_dir in discard_dirs:
                logger.log("===> Unstage {0} since PR is closed.".format(discard_dir))
                shutil.rmtree(discard_dir) 
        with timeout(self.timeout_seconds()):
            for pr in prs:
                self.process_pull(pr)
        pass
