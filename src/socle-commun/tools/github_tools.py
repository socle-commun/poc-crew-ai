from crewai import Tool
from github import Github
from typing import List, Optional
from ..config.github_config import GitHubConfig

class GitHubTools:
    def __init__(self, config: GitHubConfig):
        self.config = config
        self.github = Github(config.token)
        self.org = self.github.get_organization(config.organization)

    def get_repositories(self) -> Tool:
        """Obtient la liste des repositories de l'organisation."""
        return Tool(
            name="get_github_repositories",
            description="Récupère la liste des repositories de l'organisation GitHub",
            func=lambda: [repo.name for repo in self.org.get_repos()]
        )

    def create_issue(self) -> Tool:
        """Crée une issue dans un repository."""
        return Tool(
            name="create_github_issue",
            description="Crée une nouvelle issue dans un repository GitHub",
            func=lambda repo_name, title, body: self.org.get_repo(repo_name).create_issue(title=title, body=body)
        )

    def get_pull_requests(self) -> Tool:
        """Obtient la liste des pull requests d'un repository."""
        return Tool(
            name="get_github_pull_requests",
            description="Récupère la liste des pull requests d'un repository",
            func=lambda repo_name: [pr.title for pr in self.org.get_repo(repo_name).get_pulls()]
        )

    def get_all_tools(self) -> List[Tool]:
        """Retourne tous les outils GitHub disponibles."""
        return [
            self.get_repositories(),
            self.create_issue(),
            self.get_pull_requests()
        ] 