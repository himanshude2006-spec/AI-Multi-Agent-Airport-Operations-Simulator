# AI Multi-Agent Airport Operations Simulator

## Overview

This project is an airport operations simulator built with Python and FastAPI.

The simulator models flights, runways, gates, weather, fuel levels, delays, and emergency situations. Different airport resources work as separate agents and interact during the simulation.

The main focus of the project is scheduling, simulation, APIs, databases, and event-based systems.

---

## Main Features

- Airport operation simulation
- Flight arrival and landing management
- Runway scheduling
- Gate assignment
- Fuel tracking
- Weather changes
- Emergency handling
- Flight diversions
- Live event updates
- Scheduling experiments
- Performance metrics

---

## Airport Simulation

The simulator models:

- Aircraft arrivals
- Landing queues
- Runway availability
- Gate allocation
- Fuel usage
- Weather disruptions
- Emergency landings
- Flight diversions

The simulation runs one tick at a time. Each tick updates flights, fuel, weather, runways, gates, and events.

---

## Scheduling Algorithms

The project includes:

- First Come First Served
- Fuel Priority
- Weighted Priority
- Random Scheduling
- Constraint-based Scheduling

The same scenario can be tested with different algorithms for comparison.

---

## Experiment Framework

The project supports:

- Seeded simulations
- Repeatable experiments
- Multiple scheduling strategies
- Performance comparisons
- Batch simulation runs

---

## Metrics

The simulator tracks:

- Average delay
- Maximum delay
- Passenger delay
- Completed flights
- Diverted flights
- Emergency count
- Runway utilization
- Gate utilization
- Throughput
- Fairness score
- Overall simulation score

---

## Tech Stack

### Main Technologies

- Python
- FastAPI
- PostgreSQL
- Redis
- Docker
- Pytest

---

## Project Statistics

- More than 8,000 lines of code
- 150 automated tests
- Multiple scheduling algorithms
- Real-time event updates
- Database and cache support

---

## Project Structure

```text
app/
    main.py

    airport/
        agents.py
        engine.py
        metrics.py
        schedule.py
        weather.py

    web/
        api.py
        events.py

    data/
        db.py
        store.py

    other/
        ai.py
        settings.py
        tasks.py
        types.py

tests/

Dockerfile
docker-compose.yml
requirements.txt
```

---

## API

The API can be used to:

- Create simulations
- Add flights, runways, and gates
- Generate sample airport data
- Run one or more simulation ticks
- Run a complete simulation
- View simulation state
- View events
- View metrics
- Compare scheduling algorithms
- Stream live events

---

## Setup

Install the required packages and configure the database and Redis settings.

Start the required services and run the FastAPI application.

Docker Compose can also be used to start the project.

Open the FastAPI documentation page to test the available endpoints.

---

## Testing

Pytest is used for automated testing.

The tests cover the API, simulation engine, airport agents, scheduling algorithms, events, metrics, and experiment runs.

Run the tests using:

```bash
pytest
```
