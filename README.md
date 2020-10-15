# Salt_Finger_Diffusion_Simulation
(More info TBA later)
With the Supervision of Dr. N. Grisouard and Dr. B. Zemskova from April 2020 to August 2020.
What is included is the basic code structure for the simulation of Salt fingers and Oscillative Diffusion in bodies of water and studying how oxygen is distributed in it. The code is in UNIX, python and fortran and is visualized using visIt and python. The entire code is not posted here, but the basic structure of the code is included. Nek5000 solver, which is in fortran, was used to calculate the simulations and the states and Python and its libraries was used to calculate values such as advective flux and diffusive flux.

The simulations were conducted by inputting the Non-dimensionalized Boussinesq Equations (Navier Stokes Equations) into the Nek5000 Solver along with the linear equation of state between temperature and salinity. In my simulations, I investigated the effect of the density ratio in salt fingers and oscillative diffusion in the ocean. Furthermore, by changing such parameters, I also looked at how oxygen is distrubuted in the model especially as staircases of temperature and salinity start forming.

# Results
See Results at: https://docs.google.com/presentation/d/1XVgVNwTVRHH1cFl-tbmP9pR_yeeAeySQ-jE2b_siUDY/edit?usp=sharing

# Acknowlegdement
1. Nek5000:
  - https://github.com/Nek5000/Nek5000 Github
  - https://nek5000.mcs.anl.gov/ Official Site
  - https://github.com/yvielcastillejos/pymech Pymech
2. VisIt: 
  - https://wci.llnl.gov/simulation/computer-codes/visit/ Website
