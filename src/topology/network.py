import networkx as nx


class OTNetworkTopology:
    """
    Represents a simulated OT network as a graph.
    """

    def __init__(self) -> None:
        self.graph = nx.Graph()

    def add_device(
        self,
        device_id: str,
        device_type: str,
        location: str
    ) -> None:
        """
        Add an OT device to the topology.
        """
        self.graph.add_node(
            device_id,
            device_type=device_type,
            location=location
        )

    def add_link(
        self,
        source: str,
        destination: str,
        medium: str = "fiber"
    ) -> None:
        """
        Add a communication link.
        """
        if source not in self.graph:
            raise ValueError(f"Unknown source device: {source}")

        if destination not in self.graph:
            raise ValueError(
                f"Unknown destination device: {destination}"
            )

        self.graph.add_edge(
            source,
            destination,
            medium=medium,
            status="UP"
        )

    def set_link_status(
        self,
        source: str,
        destination: str,
        status: str
    ) -> None:
        """
        Change the state of a communication link.
        """
        if not self.graph.has_edge(source, destination):
            raise ValueError(
                f"Link does not exist: {source} -> {destination}"
            )

        self.graph[source][destination]["status"] = status

    def get_devices(self):
        """
        Return devices currently represented in the topology.
        """
        return list(self.graph.nodes(data=True))

    def get_links(self):
        """
        Return network links currently represented.
        """
        return list(self.graph.edges(data=True))
