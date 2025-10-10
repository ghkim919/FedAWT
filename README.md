# FedAWT
This repository is for the data availability of the FedAWT paper.
The structure of this repository is as follows.
- simulation: Simulation Code (The integrated execution code version preparation in progress)
- data: Collection of results data used in the paper(train acc, loss, drop date). Additional data will be uploaded later.

# Simulation Requirements
- python : 3.9
- tensorflow : 2.11

# Repository Structure
```
.
├── data
│   ├── CIFAR_10
│   │   ├── DPSGD_ALPHA1.0_BETA2.5_BATCH32.csv
│   │   ├── DPSGD_ALPHA1.75_BETA1.75_BATCH32.csv
│   │   ...
│   │   └── GossipFL_ALPHA2.5_BETA1.0_BATCH32.csv
│   ├── Fashion_MNIST
│   │   ├── DPSGD_ALPHA1.0_BETA2.5_BATCH32.csv
│   │   ├── DPSGD_ALPHA1.75_BETA1.75_BATCH32.csv
│   │   ...
│   │   └── GossipFL_ALPHA2.5_BETA1.0_BATCH32.csv
│   └── MNIST
│       ├── DPSGD_ALPHA1.0_BETA2.5_BATCH32.csv
│       ├── DPSGD_ALPHA1.75_BETA1.75_BATCH32.csv
│       ...
│       └── GossipFL_ALPHA2.5_BETA1.0_BATCH32.csv
├── README.md
└── simulation
    └── temp
```