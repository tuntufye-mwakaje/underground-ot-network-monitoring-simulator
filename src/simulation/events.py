from dataclasses import dataclass
from datetime import datetime


@dataclass
class OTEvent:
    """
    Represents an operational event in the simulator.
    """

    event_id: str
    event_type: str
    severity: str
    source: str
    message: str
    timestamp: datetime
  
