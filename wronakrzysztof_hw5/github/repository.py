import requests
import base64
import github.file


class Repository:
    """
    Contains file objects in dictionary files.
    get_repository downloads repository code using requests to github api.
    """

    def __init__(self, authentication):
        self.authentication = authentication
        self.files = {}

    def get_repository(self, user, repository):
        """
        Downloads repo called repository from user.
        :param user:
        :param repository:
        :return: none
        """

        # With this request I can url to request the list of all user repositories.
        repos_url = requests.get('https://api.github.com/users/' + user, auth=self.authentication).json()['repos_url']

        # This request will obtain the list of all repositories.
        repositories_response = requests.get(repos_url, auth=self.authentication).json()

        # I __get_repo_url_by_name to obtain url of repository I want to use.
        commits_url = self.__get_repo_url_by_name(repository, repositories_response)

        # Request to obtain all commits to the repository.
        response_commits = requests.get(commits_url, auth=self.authentication).json()  # all commits

        # Get url to final commit version of repository.
        actual_repo_url = response_commits[0]['commit']['tree']['url']

        # Get the list of all files in repository.
        actual_repo_response = requests.get(actual_repo_url+"?recursive=1", auth=self.authentication).json()

        # iterate over list of files in repository and find .py ones.
        for element in actual_repo_response['tree']:
            if element['path'].endswith('.py'):
                # Creation of File object.
                new_file = github.file.File(element['path'], self.__get_file_code(element['url']))
                self.files[element['path']] = new_file

    def __get_repo_url_by_name(self, name, repos_list):
        """
        Returns url of repository called name.
        :param name: string
        :param repos_list: list
        :return: string
        """
        for repo in repos_list:
            if repo['name'] == name:
                return repo['commits_url'].split('{')[0]

    def __get_file_code(self, path):
        """
        Returns code of file under path in repository.
        :param path: string
        :return: string
        """
        response = requests.get(path, auth=self.authentication).json()
        code = base64.b64decode(response['content']).decode('utf-8')
        return code
