import boto3
import json
import os
import subprocess
import sys

# GitHub info
PR_NUMBER = os.getenv("PR_NUMBER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY")

# Claude model
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
MODEL_ID = "anthropic.claude-v2"

def run_bedrock_review(code):
    prompt = f"""
You are a senior software engineer. Review the following code and list bugs, improvements, and style suggestions:

```python
{code}
