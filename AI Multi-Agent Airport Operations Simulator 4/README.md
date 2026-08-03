# AI Multi-Agent Airport Operations Simulator

## Overview

This project is a backend simulation platform that models airport operations using autonomous software agents and an event-driven architecture.

The simulator coordinates aircraft, runways, gates, weather conditions, fuel constraints, and emergency events to evaluate different scheduling strategies under realistic operating scenarios.

The primary focus of the project is distributed systems, simulation, backend engineering, and resource scheduling.

---

## Main Features

- Airport operations simulation
- Aircraft lifecycle management
- Runway scheduling
- Gate assignment
- Weather simulation
- Fuel monitoring
- Emergency handling
- Event-driven architecture
- Real-time event streaming
- Experiment framework
- Performance benchmarking

---

## Airport Simulation

Models airport operations including:

- Aircraft arrivals
- Landing queues
- Runway availability
- Gate allocation
- Taxi operations
- Flight diversions
- Weather disruptions
- Emergency landings

---

## Scheduling Algorithms

Implemented scheduling strategies include:

- First Come First Served
- Fuel Priority
- Weighted Priority
- Constraint-based scheduling

Each strategy can be benchmarked using identical simulation scenarios.

---

## Experiment Framework

Supports:

- Seeded simulations
- Repeatable experiments
- Multiple scheduling strategies
- Performance comparisons
- Batch simulation execution

---

## Metrics

Tracks:

- Average arrival delay
- Passenger delay
- Flights completed
- Flight diversions
- Emergency events
- Runway utilization
- Gate utilization
- Overall simulation score

---

## Tech Stack

### Backend

- Python
- FastAPI

### Database

- PostgreSQL
- SQLAlchemy

### Infrastructure

- Redis
- Docker
- WebSockets

### Testing

- Pytest

---

## Project Statistics

- 80+ source files
- 30+ Python modules
- 10+ API endpoints
- 4 scheduling algorithms
- 15+ event types
- 1000+ automated tests
- 12000+ lines of code

---

## Project Structure

```text
app/
    api/
    core/
    db/
    domain/
    services/
    sim/

tests/

infra/
```

---

## API

Provides endpoints to:

- Create simulations
- Execute simulations
- Advance simulation time
- Run scheduling experiments
- Retrieve simulation state
- Retrieve performance metrics
- Stream live simulation events

---

## Setup

A standard Python environment together with the required backend services is expected before running the application.

Install the required dependencies, configure the environment, initialize the supporting services, and start the API using a standard ASGI server.
