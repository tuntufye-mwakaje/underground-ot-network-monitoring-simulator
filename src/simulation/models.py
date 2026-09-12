from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class OTDevice:
    """
    Represents a simulated Operational Technology device.
    """

    device_id: str
    device_type: str
    location: str
    ip_address: str
    status: str = "ONLINE"
    last_seen: Optional[datetime] = None

    def update_status(self, status: str) -> None:
        """
        Update the simulated device status.
        """
        allowed_statuses = {"ONLINE", "OFFLINE", "MAINTENANCE"}

        if status not in allowed_statuses:
            raise ValueError(
                f"Invalid status: {status}. "
                f"Expected one of {allowed_statuses}."
            )

        self.status = status
        self.last_seen = datetime.utcnow()
