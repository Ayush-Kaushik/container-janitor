import docker


class Janitor:
    def __init__(self):
        self.__client = docker.from_env()
        self.__exist = False
        self.__container_details = {'list': {}}

    def get_client(self):
        return self.__client

    def get_exist(self):
        return self.__exist

    def get_container_details(self):
        return self.__container_details

    def check_status(self):
        container_list = self.__client.containers.list(filters={'status': 'exited'})
        if container_list.__len__() >= 0:
            self.__exist = True
            for container in container_list:
                self.__container_details['list'][container.attrs.get('Id')] = container.attrs.get('Image')

    def remove_exited(self):
        self.__client.containers.prune()

    def remove_image(self):
        print(self.__container_details['list'])
        for container_id in self.__container_details['list']:
            print(self.__container_details['list'][container_id])
            self.__client.images.remove(self.__container_details[container_id])
        print('dangling images related to container removed!')
