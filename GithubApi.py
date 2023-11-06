import string
import datetime

import requests
from PrintHelper import *


class GithubApi:
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, token: string, username: string):

        self._token = token
        self._username = username
        self._repository = None

    def createNewRepository(self, name, isPrivate: bool = False) -> bool:
        url = self.GITHUB_API_URL + "/user/repos"
        headers = {"Authorization": "Bearer " + self._token, }
        data = {"name": name, "description": "Project " + name + " created with EpiClone",
                "homepage": "https://github.com", "private": isPrivate, "has_issues": True, "has_projects": True,
                "has_wiki": True}

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            # print_success(f"[SUCCESS] 200 : Repository '{name}' has been created successfully!")
            return True
        else:
            # print_error(f"\n[ERROR] ❌ Failed to create repository '{name}'. Details:")
            response_data = response.json()
            if 'message' in response_data:
                # print_error(f"Error Message: {response_data['message']}")
                pass
            else:
                # print_error("Error Details:" + response_data)
                pass
            return False

    def checkIfRepositoryExists(self, name) -> bool:
        url = self.GITHUB_API_URL + f"/repos/{self._username}/{name}"
        headers = {"Authorization": "Bearer " + self._token}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    def getAllRepositoriesByAnOrganization(self, organizationName: string) -> dict:
        url = self.GITHUB_API_URL + f"/orgs/{organizationName}/repos"
        headers = {"Authorization": "Bearer " + self._token}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

    def getRepository(self, repositoryUrl: string) -> dict:
        url = self.GITHUB_API_URL + f"/repos/{self._username}/{repositoryUrl}"
        headers = {"Authorization": "Bearer " + self._token}

        response = requests.get(url, headers=headers)

        self._repository = response.json()

        if response.status_code == 200:
            return response.json()

    def getCommits(self, repositoryUrl: string) -> dict:

        repo = self.getRepository(repositoryUrl)

        if repo is not None:

            url = self.GITHUB_API_URL + f"/repos/{repo['owner']['login']}/{repo['name']}/commits"

            headers = {"Authorization": "Bearer " + self._token}

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return response.json()

    def getUsername(self):
        return self._username

    def isDifferent(self, repositoryUrl: string) -> bool:
        repository_updated_at = datetime.datetime.strptime(self._repository['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
        user_repo = self.getRepository(repositoryUrl)
        github_repo_updated_at = datetime.datetime.strptime(user_repo['updated_at'] if (user_repo is not None) and 'updated_at' in user_repo else '0001-01-01T00:00:00Z','%Y-%m-%dT%H:%M:%SZ')
        if github_repo_updated_at >= repository_updated_at:
            return True
        else:
            # Check if commits are the same
            last_commit_id = self.getCommits(repositoryUrl)
            my_last_commit_id = self.getCommits(self._repository['html_url'])
            if len(last_commit_id) == len(my_last_commit_id):
                return False

            if last_commit_id[0] != my_last_commit_id[0]:
                return True

        return False
