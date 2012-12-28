from fabric.api import cd, env, local, run, task


env.hosts = ('wraithan@beta.wraithan.net',)

@task
def deploy():
    local('git push')
    with cd('/srv/http/wraithan.net'):
        run('git pull')
        run('source ~/.virtualenvs/wraithan.net/bin/activate && make publish')
