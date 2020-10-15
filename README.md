# Salt_Finger_Diffusion_Simulation
(More info TBA later)
With the Supervision of Dr. N. Grisouard and Dr. B. Zemskova from April 2020 to August 2020.
What is included is the basic code structure for the simulation of Salt fingers and Oscillative Diffusion in bodies of water and studying how oxygen is distributed in it. The code is in UNIX, python and fortran and is visualized using visIt and python. The entire code is not posted here, but the basic structure of the code is included. Nek5000 solver, which is in fortran, was used to calculate the simulations and the states and Python and its libraries was used to calculate values such as advective flux and diffusive flux.

The simulations were conducted by inputting the Non-dimensionalized Boussinesq Equations (Navier Stokes Equations) into the Nek5000 Solver along with the linear equation of state between temperature and salinity. In my simulations, I investigated the effect of the density ratio in salt fingers and oscillative diffusion in the ocean. Furthermore, by changing such parameters, I also looked at how oxygen is distrubuted in the model especially as staircases of temperature and salinity start forming.

# Results
## See Full Report at: https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Results/Double%20Diffusion%20of%20Oxygen.pdf

Sneak peak of a small part of the results:
 - For The salt-finger simulations, we can look at different times to see how the layer formation takes place for temperature (The values are non dimensionalized Temperature):
<img src = "https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Salt.png" width = "550" height = "350">

 - For the salt finger simulation above, we study the nusselt number and look at the average of the flux (also correlated to energy) and see what transpires at the different regimes.
 <img src = "https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Nu.png"  width = "250" height = "250">
 
 - We can also take a look at oxygen mean vs time and see how it distributes very well as time progresses 
<img src = "https://github.com/yvielcastillejos/Salt_Finger_Diffusion_Simulation/blob/master/Oxyg_real.png" width = "250" height = "250">

# Acknowlegdement
1. Nek5000:
  - https://github.com/Nek5000/Nek5000 Github
  - https://nek5000.mcs.anl.gov/ Official Site
  - https://github.com/yvielcastillejos/pymech Pymech
2. VisIt: 
  - https://wci.llnl.gov/simulation/computer-codes/visit/ Website
3. Research Papers (TBA)
