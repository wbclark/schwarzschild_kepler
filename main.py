from astropy.constants import c as speed_of_light
from astropy.constants import G as gravitational_constant
from astropy.constants import M_sun as solar_mass
from astropy.constants import au as astronomical_unit
from scipy.constants import pi
import numpy as np
c = speed_of_light.value
G = gravitational_constant.value
M = solar_mass.value
au = astronomical_unit.value

# compute Schwarzschild radius of Sun
rs = 2*G*M/c**2

# approximate mass of Space Shuttle
m = 2030000

# reduced mass
mu = m*M/(m+M)

# initial position (roughly the distance of Mercury's perihelion)
x_init = (0.0, 46000000000.0)

# initial velocity
v_init = (-58980.0, 0.0)
mag_v_init = np.sqrt(v_init[0]**2 + v_init[1]**2)

# start at time 0 as measured by a static clock at infinity
t_init = 0.0

# convert initial position to spherical coordinates in geodesic plane theta = pi/2
r_init = np.sqrt(x_init[0]**2 + x_init[1]**2)
phi_init = np.arctan2(x_init[1],x_init[0])-pi/2
# initial proper time
tau_init = 0.0

# specific angular momentum
L = np.cross(x_init, v_init)/mu

# total energy
E = (1 - rs/r_init)*m*c**2/np.sqrt(1-mag_v_init**2/c**2)
