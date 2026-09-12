# Operational Scenarios

The simulator uses controlled scenarios to represent common monitoring
and troubleshooting situations in an industrial OT environment.

## Scenario 1 — Normal Operation

All simulated devices are operational and network measurements remain
within configured thresholds.

Expected result:

- Devices remain available
- No critical alerts
- Network health remains stable

## Scenario 2 — Fibre Link Failure

A simulated communication link is marked unavailable.

Expected result:

- Link status changes to failed
- Connected devices may become unreachable
- An incident is generated
- The topology reflects the affected connection

## Scenario 3 — High Latency

Network latency is increased above a configured threshold.

Expected result:

- Warning alert generated
- Performance metric recorded
- Affected device/link identified

## Scenario 4 — Packet Loss

Packet loss is introduced into a simulated communication path.

Expected result:

- Packet-loss threshold evaluated
- Alert generated if threshold is exceeded
- Event recorded

## Scenario 5 — Device Outage

A simulated OT device changes from online to offline.

Expected result:

- Device status changes
- Availability statistic changes
- Monitoring event recorded

## Scenario 6 — Recovery

A failed device or network link returns to normal operation.

Expected result:

- Status returns to operational
- Recovery event recorded
- Availability calculation updated
