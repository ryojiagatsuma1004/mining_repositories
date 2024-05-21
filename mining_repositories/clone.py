import os
import sys
import asyncio
import subprocess
import re


def get_repository_name(repository):
    pattern = re.compile(r'https://github.com/.+/.+\.git')
    if not pattern.match(repository):
        raise ValueError(f"Invalid repository URL: {repository}")

    last_part = repository.split('/')[-1]
    # remove the .git suffix
    repo_name = last_part.replace('.git', '')
    # return the repo name
    return repo_name


async def clone_repository_async(repository, directory=''):
    if directory == '':
        command = ["git", "clone", repository, '--quiet']
    else:
        command = ["git", "clone", repository, directory, '--quiet']
    # create a process
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                   env={**os.environ, "GIT_ASKPASS": "/bin/echo"})
    # wait for the process to complete
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        error_message = f"Failed to clone {repository}: {stderr.decode()}"
        print(error_message, file=sys.stderr)

    return process.returncode


async def clone_repositories_async(repos):
    tasks = []
    for repo in repos:
        repo_url = repo['repository']

        dest_dir = repo.get('directory')
        if dest_dir is None:
            tasks.append(clone_repository_async(repo_url))
        else:
            tasks.append(clone_repository_async(repo_url, dest_dir))

    result = await asyncio.gather(*tasks, return_exceptions=True)
    return result


def main():
    # how to use
    repositories = [
        {'repository': 'https://github.com/ryojiagatsuma1004/CSVPrinter.git', 'directory': 'a'},
        {'repository': 'https://github.com/ryojiagatsuma1004/CSVPrinter.git', 'directory': 'b'},
        {'repository': 'https://github.com/ryojiagatsuma1004/CSVPrinter2.git', 'directory': 'c'}
    ]
    print("start download")
    asyncio.run(clone_repositories_async(repositories))
    print("finish download")


if __name__ == '__main__':
    main()
