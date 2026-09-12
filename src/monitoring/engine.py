from dataclasses import dataclass


@dataclass
class NetworkMetric:
    device_id: str
    latency_ms: float
    packet_loss_percent: float
    availability_percent: float


class MonitoringEngine:
    """
    Evaluates simulated network measurements.
    """

    def __init__(
        self,
        latency_threshold_ms: float = 100.0,
        packet_loss_threshold_percent: float = 5.0,
        availability_threshold_percent: float = 95.0
    ) -> None:

        self.latency_threshold_ms = latency_threshold_ms
        self.packet_loss_threshold_percent = (
            packet_loss_threshold_percent
        )
        self.availability_threshold_percent = (
            availability_threshold_percent
        )

    def evaluate(self, metric: NetworkMetric) -> list[str]:
        """
        Evaluate a network metric and return generated alerts.
        """

        alerts = []

        if metric.latency_ms > self.latency_threshold_ms:
            alerts.append(
                f"HIGH_LATENCY:{metric.device_id}"
            )

        if (
            metric.packet_loss_percent
            > self.packet_loss_threshold_percent
        ):
            alerts.append(
                f"HIGH_PACKET_LOSS:{metric.device_id}"
            )

        if (
            metric.availability_percent
            < self.availability_threshold_percent
        ):
            alerts.append(
                f"LOW_AVAILABILITY:{metric.device_id}"
            )

        return alerts
