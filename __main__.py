import pulumi
import pulumi_docker as docker

# Pull the nginx image from Docker Hub
nginx_image = docker.RemoteImage(
    "nginx-image",
    name="nginx:alpine"
)

# Create and run a container from that image, mapping port 80 -> host 8080
nginx_container = docker.Container(
    "nginx-container",
    image=nginx_image.name,
    ports=[docker.ContainerPortArgs(internal=80, external=8080)]
)

pulumi.export("container_name", nginx_container.name)
pulumi.export("container_id", nginx_container.id)
