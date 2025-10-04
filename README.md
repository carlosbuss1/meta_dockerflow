# Meta DockerFlow: Taxonomic Analysis Pipeline with Cross-Platform Reproducibility

## Project Mission

This repository demonstrates **Docker-based computational reproducibility** for taxonomic data analysis across heterogeneous computing environments. The primary goal is to ensure that taxonomic analysis workflows produce **identical results** regardless of the host operating system, hardware configuration, or local software dependencies. This project serves as a reference implementation for containerized bioinformatics pipelines, addressing common reproducibility challenges in computational biology.

![Docker Reproducibility Workflow](docker_reproducibility.png)
*Figure: Ensuring consistent taxonomic analysis across Windows, macOS, and Linux environments*

---

## Scientific Context

### The Reproducibility Challenge

Bioinformatics analyses often fail to reproduce across different computational environments due to:
- **Dependency conflicts** between software versions
- **Operating system differences** (Windows vs macOS vs Linux)
- **Library version mismatches** in Python packages
- **File permission inconsistencies** across platforms
- **Path resolution differences** between systems

### Our Solution

This pipeline implements a **fully containerized workflow** that:
- Encapsulates all dependencies in a Docker image
- Standardizes the computational environment
- Eliminates "works on my machine" problems
- Ensures bit-for-bit reproducible results
- Provides platform-agnostic execution

---

## Key Features

| Feature | Description | Reproducibility Benefit |
|---------|-------------|------------------------|
| **Containerized Environment** | Complete isolation using Docker | Eliminates host system dependencies |
| **Fixed Package Versions** | Pinned versions in Dockerfile | Ensures consistent library behavior |
| **Automated Workflow** | Single-command execution | Reduces human error in analysis |
| **Cross-Platform Testing** | Validated on Windows, macOS, Linux | Guarantees multi-OS compatibility |
| **Output Verification** | Checksums for result validation | Confirms identical outputs |
| **Permission Handling** | Built-in solutions for file access | Overcomes OS-specific restrictions |

---

## Pipeline Components

### Analysis Tasks Performed

1. **Data Validation & Quality Control**
   - Input format verification
   - Missing data detection
   - Taxonomic hierarchy validation

2. **Statistical Analysis**
   - Species count aggregation by phylum
   - Average species calculation per taxonomic level
   - Diversity metrics computation

3. **Visualization Generation**
   - Bar charts for species distribution
   - Publication-ready figures (300 DPI)
   - Automated plot formatting

4. **Result Export**
   - CSV formatted summary statistics
   - PNG visualization exports
   - Metadata documentation

---

## Repository Structure

```
meta_dockerflow/
├── Dockerfile                    # Container specification
├── requirements.txt             # Python dependencies (fixed versions)
├── taxonomic_analysis.py        # Main analysis script
├── taxonomic_data.csv          # Sample dataset
├── docker-compose.yml          # Optional: multi-container setup
├── .dockerignore              # Exclude unnecessary files
├── output/                    # Generated results (created at runtime)
│   ├── summary_statistics.csv
│   └── total_species_count_chart.png
└── README.md                  # This documentation
```

---

##  Technical Requirements

### Host System Prerequisites

- **Docker Engine**: Version 20.10.0 or later
- **Available RAM**: Minimum 2GB
- **Disk Space**: 1GB for Docker image + data
- **Operating Systems**: 
  - Windows 10/11 (WSL2 recommended)
  - macOS 10.15+ (Intel/Apple Silicon)
  - Linux (Ubuntu 20.04+, CentOS 8+, Debian 10+)

### Containerized Dependencies

The Docker image includes precisely versioned components:

```dockerfile
# Base image for reproducibility
FROM python:3.9.16-slim

# Fixed package versions
RUN pip install --no-cache-dir \
    pandas==1.5.3 \
    matplotlib==3.6.3 \
    numpy==1.24.2
```

---

##  Quick Start Guide

### One-Line Execution

```bash
# Complete pipeline execution
curl -sSL https://raw.githubusercontent.com/carlosbuss1/meta_dockerflow/main/run.sh | bash
```

### Step-by-Step Workflow

```bash
# 1. Clone the repository
git clone https://github.com/carlosbuss1/meta_dockerflow.git
cd meta_dockerflow

# 2. Build the reproducible environment
docker build -t taxonomic_analysis .

# 3. Execute the analysis
docker run --name taxo_output taxonomic_analysis

# 4. Extract results
docker cp taxo_output:/app/output ./output

# 5. Cleanup
docker rm taxo_output

# 6. Verify outputs
ls -la output/
```

---

## Reproducibility Validation

### Verifying Consistent Results

To confirm reproducibility across machines:

```bash
# Generate checksums for output files
md5sum output/* > checksums.txt

# Expected checksums (example)
# a3f2b1c4d5e6f7a8b9c0d1e2f3a4b5c6  output/summary_statistics.csv
# b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9  output/total_species_count_chart.png
```

### Cross-Platform Testing Protocol

```bash
# Test on different platforms
docker run --platform linux/amd64 --name test_amd64 taxonomic_analysis
docker run --platform linux/arm64 --name test_arm64 taxonomic_analysis

# Compare outputs
diff <(docker exec test_amd64 cat /app/output/summary_statistics.csv) \
     <(docker exec test_arm64 cat /app/output/summary_statistics.csv)
```

---

## Troubleshooting Guide

### Common Issues and Solutions

#### 1. Permission Denied Errors

**Problem**: Cannot write to mounted volumes on Linux/macOS
```bash
# Solution: Use Docker's copy command instead of volume mounting
docker cp taxo_output:/app/output ./output
```

#### 2. Windows Path Issues

**Problem**: Invalid paths on Windows systems
```bash
# Solution: Use WSL2 or Git Bash
wsl docker run --name taxo_output taxonomic_analysis
```

#### 3. Memory Limitations

**Problem**: Container killed due to memory constraints
```bash
# Solution: Increase Docker memory allocation
docker run --memory="4g" --name taxo_output taxonomic_analysis
```

#### 4. Image Build Failures

**Problem**: Network issues during package installation
```bash
# Solution: Use build cache and retry
docker build --no-cache -t taxonomic_analysis .
```

---

##  Performance Benchmarks

| Environment | Build Time | Execution Time | Output Size |
|-------------|------------|----------------|-------------|
| Ubuntu 22.04 | 45s | 2.3s | 156 KB |
| macOS 14.0 | 52s | 2.5s | 156 KB |
| Windows 11 | 68s | 3.1s | 156 KB |
| Docker Hub CI | 41s | 2.1s | 156 KB |

*Results demonstrate consistent output size across all platforms*

---

##  Extending the Pipeline

### Adding New Analysis Functions

```python
# taxonomic_analysis.py
def custom_diversity_metric(df):
    """Add your custom analysis here"""
    # Implementation
    pass
```

### Modifying Dependencies

```dockerfile
# Dockerfile
RUN pip install --no-cache-dir \
    pandas==1.5.3 \
    matplotlib==3.6.3 \
    numpy==1.24.2 \
    scikit-learn==1.2.1  # Add new dependency
```

---

##  Best Practices for Reproducibility

1. **Always pin package versions** in requirements.txt
2. **Use specific base image tags** (avoid `:latest`)
3. **Document random seeds** for stochastic processes
4. **Include data validation** steps
5. **Generate checksums** for output verification
6. **Test on multiple platforms** before release
7. **Archive Docker images** for long-term reproducibility

---

##  Contributing

We welcome contributions that enhance reproducibility:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Test on at least two different OS platforms
4. Submit a pull request with reproducibility test results

### Contribution Checklist

- [ ] Code runs in Docker without errors
- [ ] Outputs match expected checksums
- [ ] Tested on Windows/macOS/Linux
- [ ] Documentation updated
- [ ] No hardcoded paths

---

##  Citation

```bibtex
@software{buss2025metadockerflow,
  author = {Buss, Carlos E.},
  title = {Meta DockerFlow: Ensuring Reproducible Taxonomic Analysis Across Computing Environments},
  year = {2025},
  url = {https://github.com/carlosbuss1/meta_dockerflow},
  note = {Docker-based reproducibility framework for bioinformatics}
}
```

---

##  License

MIT License - See [LICENSE](LICENSE) file for details

---

##  Author

**Carlos E. Buss, PhD**  
Bioinformatics Researcher  
Signal Transduction and Metabolism Laboratory  
Université libre de Bruxelles (ULB)  
Brussels, Belgium  

 Email: carlos.eduardo.buss@ulb.be  
 Lab: [www.stmlaboratory.com](https://www.stmlaboratory.com)  
 GitHub: [@carlosbuss1](https://github.com/carlosbuss1)  
 Docker Hub: [carlosbuss/taxonomic-analysis](https://hub.docker.com/r/carlosbuss/taxonomic-analysis)

---

## Acknowledgments

- Docker Inc. for containerization technology
- The bioinformatics community for reproducibility standards
- STML Laboratory for computational resources
- Beta testers across Windows, macOS, and Linux platforms

---

##  Project Status

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker Version](https://img.shields.io/badge/docker-20.10%2B-blue)
![Platform Support](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

*Last tested: January 2025 | Version: 1.0.0*
