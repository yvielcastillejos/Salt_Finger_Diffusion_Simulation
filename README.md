# Salt_Finger_Diffusion_Simulation
(More info TBA later)
With the Supervision of Dr. N. Grisouard and Dr. B. Zemskova from April 2020 to August 2020.
What is included is the basic code structure for the simulation of Salt fingers and Oscillative Diffusion in bodies of water and studying how oxygen is distributed in it. The code is in UNIX, python and fortran and is visualized using visIt and python. The entire code is not posted here, but the basic structure of the code is included. Nek5000 solver, which is in fortran, was used to calculate the simulations and the states and Python and its libraries was used to calculate values such as advective flux and diffusive flux.

The simulations were conducted by inputting the Non-dimensionalized Boussinesq Equations (Navier Stokes Equations) into the Nek5000 Solver along with the linear equation of state between temperature and salinity. In my simulations, I investigated the effect of the density ratio in salt fingers and oscillative diffusion in the ocean. Furthermore, by changing such parameters, I also looked at how oxygen is distrubuted in the model especially as staircases of temperature and salinity start forming.

# Results
## See Full Results at: https://docs.google.com/presentation/d/1XVgVNwTVRHH1cFl-tbmP9pR_yeeAeySQ-jE2b_siUDY/edit?usp=sharing

Some results:
 - For The salt-finger simulations, we can look at different times to see how the layer formation takes place:
<img src = "https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Salt.png" width = "350" height = "250">

 - For the salt finger simulation above, we study the nusselt number and look at the average of the flux (also correlated to energy) and see what transpires at the different regimes.
 <img src = "https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Nu.png"  width = "150" height = "150">
 
 - We can also take a look at oxygen mean vs time and see how it distributes very well as time progresses 
<img src = "https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Oxyg_real.png" width = "180" height = "180">

# Acknowlegdement
1. Nek5000:
  - https://github.com/Nek5000/Nek5000 Github
  - https://nek5000.mcs.anl.gov/ Official Site
  - https://github.com/yvielcastillejos/pymech Pymech
2. VisIt: 
  - https://wci.llnl.gov/simulation/computer-codes/visit/ Website
3. Research Papers (TBA)
