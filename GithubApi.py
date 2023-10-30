import string
import requests
from PrintHelper import *

class GithubApi:

    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, token: string, username: string):

        self._token = token
        self._username = username

    def createNewRepository(self, name, isPrivate: bool = False) -> bool:
        url = self.GITHUB_API_URL + "/user/repos"
        headers = {
            "Authorization": "Bearer " + self._token,
        }
        data = {
            "name": name,
            "description": "Project " + name + " created with Epitech's Clone project",
            "homepage": "https://github.com",
            "private": isPrivate,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            print_success(f"[SUCCESS] 200 : Repository '{name}' has been created successfully!")
            return True
        else:
            print(f"\n[ERROR] ❌ Failed to create repository '{name}'. Details:")
            response_data = response.json()
            if 'message' in response_data:
                print(f"Error Message: {response_data['message']}")
            else:
                print("Error Details:", response_data)
            return False

    def checkIfRepositoryExists(self, name) -> bool:
        url = self.GITHUB_API_URL + f"/repos/{self._username}/{name}"
        headers = {
            "Authorization": "Bearer " + self._token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    def getAllRepositoriesByAnOrganization(self, organizationName: string) -> dict:
        url = self.GITHUB_API_URL + f"/orgs/{organizationName}/repos"
        headers = {
            "Authorization": "Bearer " + self._token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

    def getUsername(self):
        return self._username
