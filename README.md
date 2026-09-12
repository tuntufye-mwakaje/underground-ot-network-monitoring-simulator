# Underground OT Network Monitoring Simulator

A Python-based simulation and monitoring project designed to demonstrate
transferable Operational Technology (OT) capabilities relevant to complex
industrial and mining environments.

The project simulates an underground OT network containing devices,
network links, communication paths and operational assets. It provides
mechanisms for asset registration, network topology representation,
availability monitoring, performance analysis, fault simulation, alerting,
change logging and basic anomaly detection.

> **Important:** This is a software simulation and learning project. It does
> not connect to or control real mining equipment, SCADA systems, industrial
> controllers, communication infrastructure or production networks.

## Objective

The objective is to demonstrate how software, networking concepts, data
analysis and monitoring techniques can be combined to support the visibility,
maintenance and continuous improvement of an industrial OT environment.

The project focuses on:

- OT asset registration
- Network topology representation
- Device availability monitoring
- Network performance monitoring
- Fault and incident simulation
- Alert generation
- Change management logging
- Operational reporting
- Basic anomaly detection
- API-based access to monitoring information

## Simulated Environment

```text
                    Surface Network
                          |
                    +-----+------+
                    | OT Gateway |
                    +-----+------+
                          |
                    Fibre Backbone
                          |
              +-----------+-----------+
              |                       |
        Underground Switch A    Underground Switch B
              |                       |
        +-----+-----+           +-----+-----+
        |           |           |           |
     Sensor      Wi-Fi       SCADA       Remote
      Node        Node       Endpoint     Device
        |
     Machine
      Node
