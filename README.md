
# Structural origin of disorder-induced ion conduction in NaFePO4 cathode materials

**Rasmus Christensen <sup>1*</sup>,  Kristin A. Persson<sup>2,3</sup>, Morten M. Smedskjaer<sup>1</sup>**

<sup>1</sup> Department of Chemistry and Bioscience, Aalborg University, Aalborg, Denmark  
<sup>2</sup> Materials Science Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA  
<sup>3</sup> Materials Science and Engineering, University of California, Berkeley, Berkeley, CA, USA  


**\*** E-mail: [rasmusc@bio.aau.dk](mailto:rasmusc@bio.aau.dk)


## Supplementary Data
This repository includes the data and analysis code used in the paper listed above. 

### Folders:

#### `glass_structures`
Folder contains the glass structures from the ACE, Teter and BMP interatomic potentials, in the LAMMPS data format:

DFT structures are given as the final XDATCAR files from VASP after quenching.

#### `potential`
Potential files for the ACE potential and training data and input files

- `output_potential.yaml` and `output_potential.yace` contain the parameters for the ACE potential, formated for the use with `ASE` and `LAMMPS` respectively. See [PACEMAKER documentation](https://pacemaker.readthedocs.io/en/latest/) for more information. 
- `input.yaml` is the input yaml file used for the PACEMAKER framework for potential optimization.
- `train_data.pckl.gzip` and `test_data.pckl.gzip` is the training data generated after all iterations of active learning. 
  - Contains atomic structures as `ase.Atoms` objects with corresponding energies and forces
  - Load using: `df = pandas.read_pickle('train_data.pckl.gzip', compression='gzip')`

#### `active_learning`

 - `balace.yaml` input file for running active learning workflow from the [vitrum package](https://vitrum.readthedocs.io/en/latest/). The active learning workflow employed here was run using this [Github commit](https://github.com/R-Chr/vitrum/commit/60774c191430c3f3f3a5b014876f027bc5194d77), and is not guaranteed to work with the newest vitrum version without changes to the input file.
 - `run.py` script for executing workflow


## Citation
If you use this data or code in your research, please cite our paper:
- Christensen R, Persson KA, Smedskjær MM. Structural origin of disorder-induced ion conduction in NaFePO4 cathode materials. ChemRxiv. 2025; doi:10.26434/chemrxiv-2025-9sf4n  This content is a preprint and has not been peer-reviewed.

## Funding
This work was supported by the Danish Data Science Academy, which in turn is funded by the Novo Nordisk Foundation (NNF21SA0069429) and VILLUM FONDEN (40516).