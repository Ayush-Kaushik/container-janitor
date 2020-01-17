#
# Step 1: Get the functionality
# This program will search, log and remove stopped containers
# It will also remove the dangling image for the container
#
# Step 2: Design this according to OOP concepts
#
# Step 3: Add an api for this information
#

import docker


def main():
    client = docker.from_env()
    stopped_list = _checkstatus(client)
    if stopped_list['exist']:
        for item in stopped_list['list']:
            print(item, stopped_list['list'][item])
        _removeexited(client)
        _removeimage(client, stopped_list['list'])


# This function checks if there are any container that are stopped/ exited
# If yes then it will list the containers along with their id and image id
def _checkstatus(client):
    container_list = client.containers.list(filters={'status': 'exited'})

    for container in container_list:
        print(container.attrs)

    container_details = {'exist': False, 'list': {}}
    if container_list.__len__() >= 0:
        container_details['exist'] = True
        for container in container_list:
            container_details['list'][container.attrs.get('Id')] = container.attrs.get('Image')
    return container_details


def _removeexited(client):
    dead_list = client.containers.prune()
    print(dead_list)


def _logexited():
    print("Log container death")


# this gives complete list of images that is being used by containers
def _removeimage(client, container_details):
    for container_id in container_details:
        client.images.remove(container_details[container_id])
    print('dangling images removed!')


if __name__ == "__main__":
    main()
