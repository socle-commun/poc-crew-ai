#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv
from .crew import GitHubOrganizationCrew

def run():
    """
    Execute the GitHub management crew.
    """
    try:
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
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run() 