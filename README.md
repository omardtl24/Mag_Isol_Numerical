# Magnetic Isolation in Vacuum Diodes — Numerical Simulations & Bifurcation Analysis

This repository contains the source code and scripts used to study magnetic isolation phenomena in vacuum diodes via numerical methods. The work focuses on solving nonlinear boundary value problems and generating bifurcation diagrams to analyze how magnetic fields influence charged particle behavior and current regulation.

## 📁 Project Structure

The repository is organized into two main parts:

- **Python package:** Contains all core functionality, including numerical solvers, system definitions, and plotting utilities.
- **Scripts & Notebooks:** High-level Jupyter notebooks and Python scripts that demonstrate how to use the package, reproduce results, and generate figures.

This separation promotes clean code reuse and allows researchers to easily plug in new configurations or visualize results without modifying core logic.

## 🔧 Installation

This project runs entirely in Python. To get started:

1. Clone the repository:

```bash
git clone https://github.com/omardtl24/Mag_Isol_Numerical.git
cd Mag_Isol_Numerical/
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 📦 Main Dependencies

- **NumPy** – for numerical computations  
- **SciPy** – for differential equation solvers  
- **Matplotlib** – for rendering bifurcation diagrams and plots  
- **Jupyter** – for running and exploring interactive notebooks  

All required packages can be installed via the `requirements.txt` file included in the repository.

## 🚀 Usage

To explore the simulations and plots interactively:

```bash
jupyter notebook
```

and look around the scripts folder.
