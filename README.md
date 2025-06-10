
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
- `train_data.pckl.gzip` and `test_data.pckl.gzip` is the training data generated after all iterations of active learning. The files contain all atomic structes as `ase.Atoms` objects, along with their corresponding energy and forces. Files can be read with `pandas` as  `df = pandas.read_pickle(train_data.pckl.gzip, compression="gzip")`.

#### `active_learning`

 - `balace.yaml` input file for running active learning workflow from the [vitrum package](https://vitrum.readthedocs.io/en/latest/). The active learning workflow employed here was run using this [Github commit](https://github.com/R-Chr/vitrum/commit/60774c191430c3f3f3a5b014876f027bc5194d77), and is not guarenteed to work with the newest vitrum version without changes to the input file.
 - `run.py` script for executing workflow