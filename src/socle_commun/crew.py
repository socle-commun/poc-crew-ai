import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CrewaiEnterpriseTools

@CrewBase
class GitHubOrganizationCrew:
    """Crew pour la gestion d'une organisation GitHub"""

    @agent
    def github_manager(self) -> Agent:
        enterprise_actions_tool = CrewaiEnterpriseTools(
            enterprise_token=os.getenv("CREWAI_ENTERPRISE_TOOLS_K"),
            actions_list=[
                "github_update_issue",
                "github_get_issue_by_number",
                "github_create_release",
                "github_update_release",
                "github_get_release_by_id",
                "github_get_release_by_tag_name",
                "github_search_issue",
                "github_lock_issue",
            ],
        )
        return Agent(
            config=self.agents_config["github_manager"],
            tools=[*enterprise_actions_tool],
        )

    @task
    def manage_github_projects(self) -> Task:
        return Task(
            config=self.tasks_config["manage_github_projects"],
        )

    @crew
    def crew(self) -> Crew:
        """Crée le crew de gestion GitHub"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        ) 