from src import nodes
import json


class AWSLoader:
    def __init__(self, resources: list = None):
        self.resources = resources

    @staticmethod
    def node_classess():
        """Return the available AWS nodes by the class alias

        Returns:
            _type_: _description_
        """
        node_mapping = {cls.__dict__['__alias__']: cls for name, cls in nodes.__dict__.items()
                        if name.startswith('AWS') and cls.__dict__['__type__'] == "AWSResource"}
        return node_mapping

    @staticmethod
    def node_models(path: str):
        """_summary_

        Args:
            path (str): _description_

        Returns:
            _type_: _description_
        """
        with open(path, 'r') as configfile:
            configobject = json.loads(configfile.read())
        resources = [nodes.ConfigItem(**item) for item in configobject['configurationItems']]
        return resources

    @classmethod
    def from_config_file(cls, path: str):
        """Load objects from an AWS Config export (json formatted)

        Args:
            path (str): _description_

        Returns:
            _type_: _description_
        """
        with open(path, 'r') as configfile:
            configobject = json.loads(configfile.read())

        node_models = AWS.node_classess()
        resources = [node_models[item['resourceType']](**item) for item in configobject['configurationItems'] 
                     if item['resourceType'] in node_models]
        return cls(resources=resources)