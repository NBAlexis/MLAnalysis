# MLAnalysis

MLAnalysis is a simple python tool to analysis Les Houches Event data files and LHC Olympic data files.

## Installation

To install Your Program Name, follow these steps:

1. Clone the repository to your local machine.
2. Optionally MLAnalysis can work with numpy and matplotlib

## Usage

To use MLAnalysis, follow these steps:

1. Before using MLAnalysis, an LHE or LHCO file is needed.
2. Write your own analysis, such as:

```python
from Interfaces.LHCOlympics import LoadLHCOlympics

events = LoadLHCOlympics("yourfilename.lhco")
cut = yourCut()
CutEvents(events, cut)

```

## Directory Structure

MLAnalysis should have the following directory structure:

```
.
├── Applications/
│   ├── AAWW/
│   ├── AW/
│   └── AZ/
│   └── ...
├── CEVisualize/
├── CutAndExport/
├── DataStructure/
├── Interfaces/
├── __init__.py
└── README.md

The `Applications/` directory contains subdirectories for different applications, many of them have already been used in previous studies. 
The `CutAndExport/` directory contains files implementing the cut functionality.
The `DataStructure/` directory contains files maintaining the events.
The `Interfaces/` directory contains functions to load the LHE and LHCO files.

## Contributing

If you'd like to contribute to Your Program Name, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and commit your changes.
4. Push your changes to your forked repository.
5. Open a pull request to merge your changes into the main repository.

Thank you for using MLAnalysis! If you have any questions or issues, please don't hesitate to reach out to me at yangjichong@lnnu.edu.cn.
