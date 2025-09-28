# Pulumi Docker Demo

Simple Pulumi Python demo that pulls the nginx image and runs a container mapped to host port 8080.

## Prerequisites

- Python 3.8+
- Docker installed and running
- Git

## Setup

```bash
# Clone the repo
git clone https://github.com/d3vanshhhh/pulumi-docker-demo.git
cd pulumi-docker-demo

# Create a Python virtual environment
python -m venv venv
# Activate the venv (Windows)
.\venv\Scripts\Activate.ps1
# macOS/Linux
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Login Pulumi locally
pulumi login --local

# Create the stack
pulumi stack init dev

# Deploy the container
pulumi up

# Open in browser
http://localhost:8080

# Destroy when done
pulumi destroy
