import argparse
parser = argparse.ArgumentParser(prog = 'uv for i-th redshift')
parser.add_argument('--zi', type=int, default=0, choices=range(2107))
inputs = parser.parse_args()

import numpy as np
import tools21cm as t2c
t2c.const.set_hubble_h(0.678)
t2c.const.set_omega_matter(0.308)
t2c.const.set_omega_baryon(0.048425)
t2c.const.set_omega_lambda(0.692)
t2c.const.set_ns(0.968)
t2c.const.set_sigma_8(0.815)

Redshifts = ['006.00060', '006.75589', '007.63960', '008.68274', '009.92624', '011.42503', \
            '013.25424', '015.51874', '018.36856', '022.02434', '026.82138', '033.28927', '034.50984']

d0 = t2c.cosmology.z_to_cdist(float(Redshifts[0]))
cdist = np.array(range(2107 + 1))*1.5 + d0 #adding one more redshit to the end
# print(cdist)
redshifts = t2c.cosmology.cdist_to_z(cdist)
redshifts_mean = (redshifts[:-1] + redshifts[1:]) / 2
# print(redshifts)
# print(redshifts.shape)
# print(redshifts_mean.shape)

# uv, N_ant = t2c.noise_model.make_uv_map_lightcone(ncells=200, zs=redshifts_mean, boxsize=300)
uv, N_ant = t2c.noise_mode.get_uv_map(ncells=200, zs=redshifts_mean[inputs.zi], boxsize=300)
print(N_ant)
np.save(f'uv_{inputs.zi}.npy', uv)
