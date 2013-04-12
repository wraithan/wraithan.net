from fabric.api import cd, env, run, task


env.hosts = ('wraithan@beta.wraithan.net',)


@task
def deploy():
    with cd('/srv/http/wraithan.net'):
        run('git pull')
        run('source ~/.virtualenvs/wraithan.net/bin/activate && make publish')
