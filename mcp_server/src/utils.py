import os
import requests
import base64
from github import Github
import asyncio
import requests
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

class GitHubUtils:
    @staticmethod
    def get_github_file_content(repo_name, file_path, branch='main'):
        url = f'https://raw.githubusercontent.com/{repo_name}/{branch}/{file_path}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            raise Exception(f'Error fetching file: {response.status_code}')

    @staticmethod
    def get_ai_discovery_schema():
        repo_name = '1155project/ai_discovery_specification/refs/heads'
        file_path = 'spec/well_known_ai_discovery_schema.json'
        return GitHubUtils.get_github_file_content(repo_name, file_path)

    @staticmethod
    def get_ai_discovery_spec_document():
        repo_name = '1155project/ai_discovery_specification/refs/heads'
        file_path = 'spec/ai_discovery_meta_specification.md'
        return GitHubUtils.get_github_file_content(repo_name, file_path)
