# AI4LIFE Utils

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Lightweight collection of data transformation and processing utilities used by the AI4LIFE project. This repository contains scripts and helpers for preparing, validating, and transforming student essays, transcripts, and related auxiliary data for downstream NLP and evaluation tasks.

Why use this repo
- Provides repeatable pipelines to transform raw essay datasets into analysis-ready formats.
- Small, focused scripts that are easy to adapt and extend for new datasets or preprocessing needs.
- Includes quick quality checks, baseline model orchestration, and transcript processing tools.

Quick links
- Main data transformer: [pivot.py](pivot.py)  
- Dataset checks: [checkDatasets.py](checkDatasets.py)  
- Baseline model starter: [baselineModel.py](baselineModel.py)  
- Essay rater/scorer helper: [rate.py](rate.py)  
- Transcript helper: [transcript.py](transcript.py)  
- Example data / reference files: [transcripts_for_qa_extraction.json](transcripts_for_qa_extraction.json)  
- Dependencies: [requirements.txt](requirements.txt)  
- License: [LICENSE](LICENSE)

Repository layout
- data/ — Local dataset inputs and processed outputs. Keep raw/processed in organized subfolders.
- transcripts/ — Transcript inputs used by `transcript.py`.
- pivot.py — Core script to pivot and transform essay dataset formats into standard analysis layouts.
- baselineModel.py — Minimal baseline model/runner for quick comparisons.
- rate.py — Scoring and rating utilities used by evaluation workflows.
- checkDatasets.py — Sanity checks and dataset validators for expected schema/fields.
- transcript.py — Utilities for converting and filtering transcript files.
- transcripts_for_qa_extraction.json — Example transcript JSON used for QA extraction experiments.
- check.txt — Short README/checks log (workspace-specific).

Getting started (developer)
1. Clone the repository and move into it:
   ```bash
   git clone https://github.com/long7872/HireMe-utils.git
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

## Example usage

1. Run the main data transformation pipeline:
   ```sh
   python pivot.py
   ```

See the top of [pivot.py](pivot.py) for any script-specific CLI arguments or constants to adjust

2. Validate datasets:
   ```sh
   python checkDatasets.py
   ```

3. Run a simple baseline model or quick evaluation:
   ```sh
   python baselineModel.py
   python rate.py
   ```

4. Process transcript files / generate QA extraction input:
   ```sh   
   python transcript.py --input transcripts/ --output data/processed_transcripts/
   # Example data file: transcripts_for_qa_extraction.json
   ```

## Notes and conventions

Input CSVs and JSONs should be placed under data (or processed where appropriate). See pivot.py for expected input schemas.
Scripts are intentionally script-first (single-file) — they are easy to read and modify for custom dataset pipelines.
Keep raw data out of Git and store only metadata or small example files checked into the repo.

## Tests and validation

This repository does not include a formal test suite at present. Use checkDatasets.py for dataset-level validations and add unit tests in tests/ if you intend to harden conversions.
Where to get help

Open an issue in the repository for bugs, requests, or questions.
Ask the AI4LIFE engineering team or maintainers for guidance on dataset-specific concerns.

## Contributing

Contributions are welcome. Please:
Fork and create a feature branch
Add tests for new functionality where possible
Keep changes small and well described
Submit a pull request for review

See CONTRIBUTING.md (if available) or open an issue to discuss larger changes.

## Maintainers

Maintained by the AI4LIFE engineering team. For ownership or access questions, open an issue in this repository.
License

This project is licensed under the terms in [LICENSE](LICENSE).

## Acknowledgements

Core utilities and experiments for essay analysis and QA pipeline support the broader AI4LIFE research workflows.