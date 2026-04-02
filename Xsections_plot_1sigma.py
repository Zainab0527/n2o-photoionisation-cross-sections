import numpy as np
import matplotlib.pyplot as plt


our_data = np.loadtxt('cross-sections-1sigma.txt', delimiter=':')
E_our = our_data[:, 0]
sigma_our = our_data[:, 1]


exp_data = np.loadtxt('lit_Xsec_experiment.csv', delimiter=',')
E_exp = exp_data[:, 0]
sigma_exp = exp_data[:, 1]

rchf_data = np.loadtxt('lit_Xsec_RCHF.csv', delimiter=',')
E_rchf = rchf_data[:, 0]
sigma_rchf = rchf_data[:, 1]

fchf_data = np.loadtxt('lit_Xsec_FCHF.csv', delimiter=',')
E_fchf = fchf_data[:, 0]
sigma_fchf = fchf_data[:, 1]


plt.figure(figsize=(8, 6))


plt.plot(E_rchf, sigma_rchf,
         color='black', linewidth=2,
         label='RCHF (literature)')

plt.plot(E_fchf, sigma_fchf,
         color='black', linestyle='--', linewidth=2,
         label='FCHF (literature)')


plt.scatter(E_exp, sigma_exp,
            color='black', s=25,
            facecolors='black',
            label='Experiment (literature)')


plt.plot(E_our, sigma_our, marker='o', 
         color='red', markersize=4, markevery=2, linewidth=2,
         label='Our Cross-section calculations')



plt.xlabel('Photon energy (eV)', fontsize=12)
plt.ylabel('Cross section (Mb)', fontsize=12)

plt.xlim(540, 600)
plt.ylim(0, 1.0)

plt.grid(False)
plt.legend(frameon=False, fontsize=11)
plt.title(r'$1\sigma$ Photoionisation Cross Section of N$_2$O')


plt.axvline(x=541.2, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='O 1s threshold')

plt.tight_layout()
plt.savefig('1sigma_cross_section_plots.png', dpi=300)
plt.show()