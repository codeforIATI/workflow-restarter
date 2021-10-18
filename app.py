from os import environ
import time

import requests


def request(method, path, prefix="https://api.github.com/repos/",
            sleep=0.5, **kwargs):
    headers = {
        'Authorization': 'token {}'.format(
            environ.get("GH_TOKEN"))}
    resp = requests.request(method, prefix + path, headers=headers, **kwargs)
    resp.raise_for_status()
    time.sleep(sleep)
    return resp


def enable_repo_workflow(repo, id_):
    request("put", repo + f"/actions/workflows/{id_}/enable")
    print(f"Enabled workflow for repo: {repo}, workflow: {id_}")


def enable_repo_workflows(repo):
    j = request("get", repo + "/actions/workflows").json()
    for workflow in j["workflows"]:
        if workflow["state"] != "active":
            id_ = workflow["id"]
            enable_repo_workflow(repo, id_)


def read_repos_from_file(filename="repos.txt"):
    with open(filename) as f:
        repos = f.read().split("\n")
    return [
        repo.split("https://github.com/")[1]
        for repo in repos
        if repo]


if __name__ == '__main__':
    repos = read_repos_from_file()
    for repo in repos:
        enable_repo_workflows(repo)
