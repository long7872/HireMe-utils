# AI4LIFE Utils

A data processing and utilities repository for the AI4LIFE project, providing tools for preprocessing and analyzing essay datasets.

## Overview

This repository contains Python scripts and utilities for transforming and analyzing educational essay data. The primary tool is [pivot.py](pivot.py), which handles core data transformations across multiple essay datasets.

## Features

- **Data transformation pipeline** — Convert and pivot essay datasets into analysis-ready formats
- **Multi-dataset support** — Process various essay sets (e.g., essay_set1, essay_set6, essay_set_12_all)
- **Structured output** — Generate processed datasets in standardized formats
- **Dependency management** — Easy setup with Python virtual environments

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Git

### Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd AI4LIFE/utils
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main data processing pipeline:

```sh
python pivot.py
```

The script will process dataset files from the `data/` directory and output transformed results.

### Input Data

Place CSV files in the `data/processed/` directory. Expected format:
```csv
id,score1,score2,score3,score4,essay_text
```

### Output

Processed files are generated in the `data/` directory with pivoted or transformed structures ready for analysis.

## Project Structure

```
.
├── pivot.py              # Main data transformation script
├── requirements.txt      # Python package dependencies
├── README.md             # This file
├── LICENSE               # Project license
├── .gitignore            # Git exclusion rules
└── data/                 # Dataset files (not tracked in version control)
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes and test thoroughly
4. Commit with clear messages (`git commit -m 'Add feature description'`)
5. Push and open a pull request

Please ensure code follows project conventions and update this README if adding new scripts or functionality.

## License

This project is licensed under the terms specified in [LICENSE](LICENSE).

## Support

For questions or issues, please open a GitHub issue in the repository.