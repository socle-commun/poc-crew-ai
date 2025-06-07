#!/usr/bin/env python
import os
from dotenv import load_dotenv
from socle_commun.crew import GitHubOrganizationCrew

def run():
    """
    Execute the GitHub management crew.
    """
    # Load environment variables
    load_dotenv()
    
    # Verify required environment variables
    required_vars = ["CREWAI_ENTERPRISE_TOOLS_K", "GITHUB_ORGANIZATION", "GITHUB_PROJECT_NAME"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    inputs = {
        "organization": os.getenv("GITHUB_ORGANIZATION"),
        "project_name": os.getenv("GITHUB_PROJECT_NAME")
    }
    
    crew = GitHubOrganizationCrew().crew()
    result = crew.kickoff(inputs=inputs)
    return result

if __name__ == "__main__":
    run() 