# Geospatial Database Benchmark
**[Português (BR)](README.pt-BR.md) | English**

### Research Proposal (Scientific Initiation)

**Student:** Giovanna Oliveira Ledo de Souza
**Project Title:** Performance and Architecture Analysis of Spatio-Temporal Databases under High-Concurrency Scenarios

### 1. The Problem
Modern systems that handle location data — such as fleet tracking, delivery apps, and drone route analysis — generate massive volumes of geographic data every second. The main technical challenge is that if the database is not optimized for coordinates (latitude/longitude), the system becomes slow, crashing queries and affecting operations. This project proposes a comparative performance analysis between two database models: relational **PostgreSQL with PostGIS** and NoSQL **MongoDB**, evaluating how each handles real geospatial data under high-stress scenarios (multiple simultaneous accesses). Additionally, a caching layer using **Redis** will be evaluated to optimize queries.

### 2. Justification and Relevance
The choice of database architecture directly impacts infrastructure costs (RAM consumption) and user experience (latency).
*   **Scientific Gap:** Current literature lacks tests using real, noisy data (like drone and GPS trajectories) under high-concurrency simulations. Most studies use synthetic data and isolated queries.
*   **Practical Relevance:** Deeply understanding spatial indexes (such as PostGIS *R-Tree* and MongoDB *2dsphere*) is essential for designing scalable smart city and monitoring systems.
*   **Academic Alignment:** The project bridges the Software Engineering and Database background with real geolocation applications, paving the way for advanced research in GIS.

### 3. Methodology
The study will be conducted as applied experimental research (benchmarking), following these steps:
1.  **Data Acquisition:** Use of public real trajectory datasets (e.g., drone or vehicle GPS data) to ensure tests reflect real-world complexity.
2.  **Environment Setup:** Installation and configuration of PostgreSQL/PostGIS, MongoDB, and Redis (isolated via Docker for environment standardization).
3.  **Data Ingestion:** Development of Python scripts to populate the databases with geographic records and create the appropriate spatial indexes.
4.  **Stress Test:** Use of tools (like Locust or JMeter) to simulate hundreds of simultaneous proximity queries (e.g., *"find all vehicles within a 5 km radius"*).
5.  **Metrics Collection and Analysis:** Measurement of response time (latency in milliseconds) and RAM consumption for each solution. Results will be documented in comparative charts to support the conclusion on which architecture is most efficient for each type of workload.

---
*This project is part of an Undergraduate Research (Scientific Initiation) initiative and aims to support a future Master's application in Geographic Information Systems.*
