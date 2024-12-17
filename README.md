# Taxonomic Analysis Pipeline Overview

This repository provides a Python-based pipeline to analyze taxonomic data, calculate summary statistics, and generate visualizations. It is containerized using Docker for reproducibility, ensuring consistent results across different environments. The pipeline includes a sample dataset (`taxonomic_data.csv`) for testing and supports user-defined taxonomic data.

---

## Features

- **Reproducible Environment**: Leverages Docker for an isolated and consistent computational environment.
- **Flexible Input**: Works with user-defined taxonomic data in CSV format.
- **Organized Outputs**: All results are saved to the `output/` directory for easy access.
- **Customizable Analysis**: Easily extendable for various taxonomic or ecological datasets.
- **Visualization**: Generates bar charts for intuitive data presentation.
- **Robust Debugging**: Includes solutions for common issues such as permission errors, volume management, and file handling.

---

## Tasks Performed

1. **Data Input Validation**:  
   - Reads and validates the structure of the input file (`taxonomic_data.csv`).
   - Ensures proper formatting for downstream tasks.

2. **Taxonomic Analysis**:  
   - Calculates total species count for each taxonomic phylum.  
   - Computes average species count per species within each phylum.

3. **Result Generation**:  
   - Outputs processed results to the `output/` directory.  
   - Provides insights suitable for visualization or further statistical analysis.

4. **Visualization**:  
   - Generates a bar chart showing total species count per phylum.

5. **Reproducibility**:  
   - Fully automated via Docker, ensuring the same results across different environments.

---

## Deliverables

- **Processed Output Files**:  
   - `summary_statistics.csv`: Table with total and average species count per phylum.  
   - `total_species_count_chart.png`: Bar chart visualization.

- **Docker Environment**: Pre-configured container for running the pipeline without dependency issues, including solutions for host permission problems.

- **Sample Dataset**: A sample input file (`taxonomic_data.csv`) for testing the pipeline functionality.

- **Comprehensive Documentation**: This README and in-script comments to guide users through usage and customization.

---

## Prerequisites

1. **Docker**  
   Ensure Docker is installed and running on your system.  
   Minimum required version: **Docker 20.10.0** or later.  
   [Install Docker](https://docs.docker.com/get-docker/) if not already installed.

---

## Dependencies Encapsulated in the Docker Container

The following Python libraries are pre-installed and configured inside the Docker container:

- **`pandas`**: For processing tabular data and performing data analysis.
- **`matplotlib`**: For creating visualizations.
- **`numpy`**: For efficient numerical computations.

---

## Usage

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/carlosbuss1/meta_dockerflow.git
cd meta_dockerflow

---

### 2. **Build the Docker Image**

Build the Docker image using the `Dockerfile`:

```bash
docker build -t taxonomic_analysis .

---

### 3. **Run the Pipeline**

Run the container to execute the taxonomic analysis:

```bash
docker run --name taxo_output taxonomic_analysis

---

### 4. **Retrieve the Output Files**

Once the container has finished running, copy the output files to your local `output/` directory:

```bash
docker cp taxo_output:/app/output ./output

---

### 5. **Clean Up**

After retrieving the results, remove the container to free up resources:

```bash
docker rm taxo_output

---

## Outputs

After running the pipeline, the following files will be available in the `output/` directory:

1. **`summary_statistics.csv`**  
   - CSV file containing total and average species counts per phylum.

2. **`total_species_count_chart.png`**  
   - Bar chart visualizing the total species count per phylum.

---
## Debugging Notes

### 1. **Host Directory Permission Issues**

If you face permission errors when mounting a directory, avoid mounting the volume and instead copy the results using the `docker cp` command as shown above.

---

### 2. **Rebuilding the Image**

If any file is modified, rebuild the Docker image:

```bash
docker build -t taxonomic_analysis .

---

## Summarized Workflow

```bash
# Clone repository
git clone https://github.com/carlosbuss1/meta_dockerflow.git
cd meta_dockerflow

# Build the image
docker build -t taxonomic_analysis .

# Run the analysis
docker run --name taxo_output taxonomic_analysis

# Retrieve the output files
docker cp taxo_output:/app/output ./output

# Remove the container
docker rm taxo_output

---

## Contact

For questions or issues, please open a GitHub issue or contact me via [carlosbuss1](https://github.com/carlosbuss1).





