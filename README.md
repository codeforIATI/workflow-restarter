# Workflow restarter

Restart stopped workflows.

## What is this?

If a repo has been “inactive” for 60 days, GitHub switches off any scheduled workflows. This is a pain for scheduled workflows that do something important, but don’t amend the default branch.

This repo has a workflow that attempts to keep those workflows running, using the GitHub API.

The list of repos this runs on is defined in [repos.txt](https://github.com/codeforIATI/workflow-restarter/blob/main/repos.txt).
