# System Architecture

## Overview

The simulator is organized into independent components representing
monitoring, simulation, topology, persistence and API access.

## Logical Architecture

```text
User
 |
 v
Dashboard / API Client
 |
 v
FastAPI
 |
 +------------------------+
 |                        |
 v                        v
Monitoring Engine      Asset Register
 |                        |
 v                        v
Simulation Engine      SQLite
 |
 +------------+------------+
 |            |            |
 v            v            v
Devices      Links       Events
 |
 v
Topology Model
