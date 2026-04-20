
# N2O Photoionisation Cross-Sections

Code repository for the MSci Physics project report:
**"Core-Level Photoionisation Cross-Sections of N2O: Shape Resonances from a 
Hartree-Fock Single-Centre Expansion Approach"**

Zainab Sidat, University College London, 2026  
Supervisor: Prof Agapi Emmanouilidou

---

## Contents

### MOLPRO Input
- `molpro_neutral_N2O.inp` — Hartree–Fock bound orbital calculation 
for ground-state neutral N2O using the aug-cc-pVQZ basis set in C2v 
symmetry. Output was written to a MOLDEN file for use in the 
subsequent single-centre expansion calculation.

### Plotting Scripts
- `plot_1sigma.py` — Plots the partial photoionisation cross-section 
for the 1σ molecular orbital, overlaid with the experimental and 
theoretical data of Schmidbauer et al. (1991).

- `plot_2sigma.py` — Plots the partial photoionisation cross-section 
for the 2σ molecular orbital, overlaid with the experimental and 
theoretical data of Schmidbauer et al. (1991).

- `plot_3sigma.py` — Plots the partial photoionisation cross-section 
for the 3σ molecular orbital, overlaid with the experimental and 
theoretical data of Schmidbauer et al. (1991).

---

## Notes

The continuum wavefunctions, dipole matrix elements, and 
cross-section data were computed using the single-centre expansion code. These calculations 
are not included in this repository.

Literature data for comparison plots were digitised from 
Schmidbauer et al., J. Chem. Phys. 94, 5299 (1991) using 
WebPlotDigitiser.

---

## Dependencies

The plotting scripts require:
- Python 3
- NumPy
- Matplotlib
