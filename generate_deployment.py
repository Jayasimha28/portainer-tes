import jinja2
import sys

# Parameters from the environment
environment = sys.argv[1]
version = sys.argv[2]
deployment_time = sys.argv[3]

# Load Jinja template
with open('templates/deployment.yaml.j2') as f:
    template = jinja2.Template(f.read())

# Render template with parameters
rendered = template.render(
    environment=environment,
    version=version,
    deployment_time=deployment_time
)

# Write to deployment.yaml
with open('deployment.yaml', 'w') as f:
    f.write(rendered)
