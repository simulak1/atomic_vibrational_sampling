
     Program PHONON v.6.4.1 starts on 26Jan2021 at 12:14: 3 

     This program is part of the open-source Quantum ESPRESSO suite
     for quantum simulation of materials; please cite
         "P. Giannozzi et al., J. Phys.:Condens. Matter 21 395502 (2009);
         "P. Giannozzi et al., J. Phys.:Condens. Matter 29 465901 (2017);
          URL http://www.quantum-espresso.org", 
     in publications or presentations arising from this work. More details at
     http://www.quantum-espresso.org/quote

     Parallel version (MPI), running on   128 processors

     MPI processes distributed on     1 nodes
     R & G space division:  proc/nbgrp/npool/nimage =     128

     Reading data from directory:
     ./silicon.save/

     IMPORTANT: XC functional enforced from input :
     Exchange-correlation      = PBE ( 1  4  3  4 0 0)
     Any further DFT definition will be discarded
     Please, verify this is what you really want

               file si_pbe.UPF: wavefunction(s)  3S 3P renormalized

     Parallelization info
     --------------------
     sticks:   dense  smooth     PW     G-vecs:    dense   smooth      PW
     Min          99      79     21                 8447     6041     825
     Max         100      80     22                 8454     6050     832
     Sum       12745   10185   2709              1081591   773849  106047


     Calculation of q =    0.0000000   0.0000000   0.0000000

     phonons at Gamma                                                           

     bravais-lattice index     =            0
     lattice parameter (alat)  =      10.3312  a.u.
     unit-cell volume          =    1102.6910 (a.u.)^3
     number of atoms/cell      =            8
     number of atomic types    =            1
     kinetic-energy cut-off    =     300.0000  Ry
     charge density cut-off    =    1500.0000  Ry
     convergence threshold     =      1.0E-13
     beta                      =       0.7000
     number of iterations used =            4
     Exchange-correlation      = PBE ( 1  4  3  4 0 0)


     celldm(1)=   10.33121  celldm(2)=    0.00000  celldm(3)=    0.00000
     celldm(4)=    0.00000  celldm(5)=    0.00000  celldm(6)=    0.00000

     crystal axes: (cart. coord. in units of alat)
               a(1) = (  1.0000  0.0000  0.0000 )  
               a(2) = (  0.0000  1.0000  0.0000 )  
               a(3) = (  0.0000  0.0000  1.0000 )  

     reciprocal axes: (cart. coord. in units 2 pi/alat)
               b(1) = (  1.0000  0.0000  0.0000 )  
               b(2) = (  0.0000  1.0000  0.0000 )  
               b(3) = (  0.0000  0.0000  1.0000 )  


     Atoms inside the unit cell: 

     Cartesian axes

     site n.  atom      mass           positions (alat units)
        1     Si  28.0860   tau(    1) = (    0.00000    0.00000    0.00000  )
        2     Si  28.0860   tau(    2) = (    0.50000    0.50000    0.00000  )
        3     Si  28.0860   tau(    3) = (    0.00000    0.50000    0.50000  )
        4     Si  28.0860   tau(    4) = (    0.50000    0.00000    0.50000  )
        5     Si  28.0860   tau(    5) = (    0.25000    0.25000    0.25000  )
        6     Si  28.0860   tau(    6) = (    0.75000    0.75000    0.25000  )
        7     Si  28.0860   tau(    7) = (    0.25000    0.75000    0.75000  )
        8     Si  28.0860   tau(    8) = (    0.75000    0.25000    0.75000  )

     Computing dynamical matrix for 
                    q = (   0.0000000   0.0000000   0.0000000 )

     25 Sym.Ops. (with q -> -q+G )


     G cutoff = 4055.4035  (   8449 G-vectors)     FFT grid: (128,128,128)
     G cutoff = 3244.3228  (   6045 G-vectors)  smooth grid: (120,120,120)
     number of k points=    35
                       cart. coord. in units 2pi/alat
        k(    1) = (   0.0000000   0.0000000   0.0000000), wk =   0.0039062
        k(    2) = (   0.0000000   0.0000000   0.1250000), wk =   0.0234375
        k(    3) = (   0.0000000   0.0000000   0.2500000), wk =   0.0234375
        k(    4) = (   0.0000000   0.0000000   0.3750000), wk =   0.0234375
        k(    5) = (   0.0000000   0.0000000  -0.5000000), wk =   0.0117188
        k(    6) = (   0.0000000   0.1250000   0.1250000), wk =   0.0468750
        k(    7) = (   0.0000000   0.1250000   0.2500000), wk =   0.0937500
        k(    8) = (   0.0000000   0.1250000   0.3750000), wk =   0.0937500
        k(    9) = (   0.0000000   0.1250000  -0.5000000), wk =   0.0468750
        k(   10) = (   0.0000000   0.2500000   0.2500000), wk =   0.0468750
        k(   11) = (   0.0000000   0.2500000   0.3750000), wk =   0.0937500
        k(   12) = (   0.0000000   0.2500000  -0.5000000), wk =   0.0468750
        k(   13) = (   0.0000000   0.3750000   0.3750000), wk =   0.0468750
        k(   14) = (   0.0000000   0.3750000  -0.5000000), wk =   0.0468750
        k(   15) = (   0.0000000  -0.5000000  -0.5000000), wk =   0.0117188
        k(   16) = (   0.1250000   0.1250000   0.1250000), wk =   0.0312500
        k(   17) = (   0.1250000   0.1250000   0.2500000), wk =   0.0937500
        k(   18) = (   0.1250000   0.1250000   0.3750000), wk =   0.0937500
        k(   19) = (   0.1250000   0.1250000  -0.5000000), wk =   0.0468750
        k(   20) = (   0.1250000   0.2500000   0.2500000), wk =   0.0937500
        k(   21) = (   0.1250000   0.2500000   0.3750000), wk =   0.1875000
        k(   22) = (   0.1250000   0.2500000  -0.5000000), wk =   0.0937500
        k(   23) = (   0.1250000   0.3750000   0.3750000), wk =   0.0937500
        k(   24) = (   0.1250000   0.3750000  -0.5000000), wk =   0.0937500
        k(   25) = (   0.1250000  -0.5000000  -0.5000000), wk =   0.0234375
        k(   26) = (   0.2500000   0.2500000   0.2500000), wk =   0.0312500
        k(   27) = (   0.2500000   0.2500000   0.3750000), wk =   0.0937500
        k(   28) = (   0.2500000   0.2500000  -0.5000000), wk =   0.0468750
        k(   29) = (   0.2500000   0.3750000   0.3750000), wk =   0.0937500
        k(   30) = (   0.2500000   0.3750000  -0.5000000), wk =   0.0937500
        k(   31) = (   0.2500000  -0.5000000  -0.5000000), wk =   0.0234375
        k(   32) = (   0.3750000   0.3750000   0.3750000), wk =   0.0312500
        k(   33) = (   0.3750000   0.3750000  -0.5000000), wk =   0.0468750
        k(   34) = (   0.3750000  -0.5000000  -0.5000000), wk =   0.0234375
        k(   35) = (  -0.5000000  -0.5000000  -0.5000000), wk =   0.0039062

     PseudoPot. # 1 for Si read from file:
     ./si_pbe.UPF
     MD5 check sum: c39c59da582df4a0d9f10159256ea34e
     Pseudo is Projector augmented-wave + core cor, Zval =  4.0
     Generated using "atomic" code by A. Dal Corso v.6.3
     Shape of augmentation charge: PSQ
     Using radial grid of 1141 points,  6 beta functions with: 
                l(1) =   0
                l(2) =   0
                l(3) =   1
                l(4) =   1
                l(5) =   2
                l(6) =   2
     Q(r) pseudized with 0 coefficients 


     Mode symmetry, T_d (-43m)  point group:


     Atomic displacements:
     There are   9 irreducible representations

     Representation     1      1 modes -A_1  G_1  P_1  To be done

     Representation     2      2 modes -E    G_12 P_3  To be done

     Representation     3      3 modes -T_1  G_25 P_5  To be done

     Representation     4      3 modes -T_1  G_25 P_5  To be done

     Representation     5      3 modes -T_2  G_15 P_4  To be done

     Representation     6      3 modes -T_2  G_15 P_4  To be done

     Representation     7      3 modes -T_2  G_15 P_4  To be done

     Representation     8      3 modes -T_2  G_15 P_4  To be done

     Representation     9      3 modes -T_2  G_15 P_4  To be done



     Alpha used in Ewald sum =   2.8000
     PHONON       :     20.10s CPU     23.35s WALL



     Representation #  1 mode #   1

     Self-consistent Calculation

      iter #   1 total cpu time :    35.8 secs   av.it.:   5.2
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  6.420E-08

      iter #   2 total cpu time :    54.6 secs   av.it.:  12.4
      thresh= 2.534E-05 alpha_mix =  0.700 |ddv_scf|^2 =  8.921E-08

      iter #   3 total cpu time :    72.5 secs   av.it.:  11.6
      thresh= 2.987E-05 alpha_mix =  0.700 |ddv_scf|^2 =  6.710E-11

      iter #   4 total cpu time :    91.0 secs   av.it.:  12.0
      thresh= 8.192E-07 alpha_mix =  0.700 |ddv_scf|^2 =  3.825E-12

      iter #   5 total cpu time :   109.5 secs   av.it.:  12.3
      thresh= 1.956E-07 alpha_mix =  0.700 |ddv_scf|^2 =  7.554E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  2 modes #   2  3

     Self-consistent Calculation

      iter #   1 total cpu time :   131.9 secs   av.it.:   5.3
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  1.605E-08

      iter #   2 total cpu time :   167.8 secs   av.it.:  13.4
      thresh= 1.267E-05 alpha_mix =  0.700 |ddv_scf|^2 =  2.232E-08

      iter #   3 total cpu time :   201.8 secs   av.it.:  12.7
      thresh= 1.494E-05 alpha_mix =  0.700 |ddv_scf|^2 =  1.672E-11

      iter #   4 total cpu time :   236.9 secs   av.it.:  12.9
      thresh= 4.089E-07 alpha_mix =  0.700 |ddv_scf|^2 =  9.477E-13

      iter #   5 total cpu time :   272.6 secs   av.it.:  13.4
      thresh= 9.735E-08 alpha_mix =  0.700 |ddv_scf|^2 =  1.895E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  3 modes #   4  5  6

     Self-consistent Calculation

      iter #   1 total cpu time :   304.4 secs   av.it.:   5.0
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  6.979E-10

      iter #   2 total cpu time :   360.1 secs   av.it.:  14.0
      thresh= 2.642E-06 alpha_mix =  0.700 |ddv_scf|^2 =  1.557E-10

      iter #   3 total cpu time :   414.1 secs   av.it.:  13.7
      thresh= 1.248E-06 alpha_mix =  0.700 |ddv_scf|^2 =  3.453E-12

      iter #   4 total cpu time :   467.4 secs   av.it.:  13.5
      thresh= 1.858E-07 alpha_mix =  0.700 |ddv_scf|^2 =  2.271E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  4 modes #   7  8  9

     Self-consistent Calculation

      iter #   1 total cpu time :   499.7 secs   av.it.:   5.0
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  6.979E-10

      iter #   2 total cpu time :   554.6 secs   av.it.:  14.1
      thresh= 2.642E-06 alpha_mix =  0.700 |ddv_scf|^2 =  1.556E-10

      iter #   3 total cpu time :   609.2 secs   av.it.:  13.8
      thresh= 1.247E-06 alpha_mix =  0.700 |ddv_scf|^2 =  3.452E-12

      iter #   4 total cpu time :   663.2 secs   av.it.:  13.6
      thresh= 1.858E-07 alpha_mix =  0.700 |ddv_scf|^2 =  2.273E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  5 modes #  10 11 12

     Self-consistent Calculation

      iter #   1 total cpu time :   706.0 secs   av.it.:   5.2
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  3.142E-09

      iter #   2 total cpu time :   761.6 secs   av.it.:  14.2
      thresh= 5.606E-06 alpha_mix =  0.700 |ddv_scf|^2 =  3.937E-09

      iter #   3 total cpu time :   815.2 secs   av.it.:  13.1
      thresh= 6.275E-06 alpha_mix =  0.700 |ddv_scf|^2 =  1.774E-11

      iter #   4 total cpu time :   870.9 secs   av.it.:  14.0
      thresh= 4.212E-07 alpha_mix =  0.700 |ddv_scf|^2 =  1.736E-12

      iter #   5 total cpu time :   925.9 secs   av.it.:  14.0
      thresh= 1.317E-07 alpha_mix =  0.700 |ddv_scf|^2 =  1.606E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  6 modes #  13 14 15

     Self-consistent Calculation

      iter #   1 total cpu time :   972.6 secs   av.it.:   5.1
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  2.688E-09

      iter #   2 total cpu time :  1028.4 secs   av.it.:  14.2
      thresh= 5.185E-06 alpha_mix =  0.700 |ddv_scf|^2 =  3.554E-09

      iter #   3 total cpu time :  1081.4 secs   av.it.:  13.2
      thresh= 5.961E-06 alpha_mix =  0.700 |ddv_scf|^2 =  8.420E-12

      iter #   4 total cpu time :  1136.8 secs   av.it.:  14.1
      thresh= 2.902E-07 alpha_mix =  0.700 |ddv_scf|^2 =  4.564E-13

      iter #   5 total cpu time :  1193.2 secs   av.it.:  14.4
      thresh= 6.756E-08 alpha_mix =  0.700 |ddv_scf|^2 =  2.235E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  7 modes #  16 17 18

     Self-consistent Calculation

      iter #   1 total cpu time :  1225.5 secs   av.it.:   5.1
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  6.077E-10

      iter #   2 total cpu time :  1282.1 secs   av.it.:  14.4
      thresh= 2.465E-06 alpha_mix =  0.700 |ddv_scf|^2 =  1.300E-10

      iter #   3 total cpu time :  1337.3 secs   av.it.:  14.0
      thresh= 1.140E-06 alpha_mix =  0.700 |ddv_scf|^2 =  3.541E-12

      iter #   4 total cpu time :  1392.6 secs   av.it.:  14.0
      thresh= 1.882E-07 alpha_mix =  0.700 |ddv_scf|^2 =  3.009E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  8 modes #  19 20 21

     Self-consistent Calculation

      iter #   1 total cpu time :  1424.5 secs   av.it.:   5.0
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  2.792E-10

      iter #   2 total cpu time :  1481.3 secs   av.it.:  14.4
      thresh= 1.671E-06 alpha_mix =  0.700 |ddv_scf|^2 =  3.817E-11

      iter #   3 total cpu time :  1537.2 secs   av.it.:  14.2
      thresh= 6.178E-07 alpha_mix =  0.700 |ddv_scf|^2 =  3.770E-12

      iter #   4 total cpu time :  1593.6 secs   av.it.:  14.2
      thresh= 1.942E-07 alpha_mix =  0.700 |ddv_scf|^2 =  6.869E-14

     End of self-consistent calculation

     Convergence has been achieved 


     Representation #  9 modes #  22 23 24

     Self-consistent Calculation

      iter #   1 total cpu time :  1625.9 secs   av.it.:   5.1
      thresh= 1.000E-02 alpha_mix =  0.700 |ddv_scf|^2 =  2.177E-09

      iter #   2 total cpu time :  1681.8 secs   av.it.:  14.2
      thresh= 4.666E-06 alpha_mix =  0.700 |ddv_scf|^2 =  2.552E-09

      iter #   3 total cpu time :  1734.2 secs   av.it.:  13.1
      thresh= 5.052E-06 alpha_mix =  0.700 |ddv_scf|^2 =  1.958E-11

      iter #   4 total cpu time :  1789.4 secs   av.it.:  14.0
      thresh= 4.425E-07 alpha_mix =  0.700 |ddv_scf|^2 =  1.780E-12

      iter #   5 total cpu time :  1844.3 secs   av.it.:  14.0
      thresh= 1.334E-07 alpha_mix =  0.700 |ddv_scf|^2 =  1.598E-14

     End of self-consistent calculation

     Convergence has been achieved 

     Number of q in the star =    1
     List of q in the star:
          1   0.000000000   0.000000000   0.000000000

     Diagonalizing the dynamical matrix

     q = (    0.000000000   0.000000000   0.000000000 ) 

 **************************************************************************
     freq (    1) =      -1.302752 [THz] =     -43.455123 [cm-1]
     freq (    2) =      -1.302752 [THz] =     -43.455123 [cm-1]
     freq (    3) =      -1.302752 [THz] =     -43.455123 [cm-1]
     freq (    4) =       4.331298 [THz] =     144.476561 [cm-1]
     freq (    5) =       4.331298 [THz] =     144.476561 [cm-1]
     freq (    6) =       4.331298 [THz] =     144.476561 [cm-1]
     freq (    7) =       4.331542 [THz] =     144.484677 [cm-1]
     freq (    8) =       4.331542 [THz] =     144.484677 [cm-1]
     freq (    9) =       4.331542 [THz] =     144.484677 [cm-1]
     freq (   10) =      12.031026 [THz] =     401.311846 [cm-1]
     freq (   11) =      12.031026 [THz] =     401.311846 [cm-1]
     freq (   12) =      12.031480 [THz] =     401.326968 [cm-1]
     freq (   13) =      12.033980 [THz] =     401.410359 [cm-1]
     freq (   14) =      12.033980 [THz] =     401.410359 [cm-1]
     freq (   15) =      12.033980 [THz] =     401.410359 [cm-1]
     freq (   16) =      13.429451 [THz] =     447.958282 [cm-1]
     freq (   17) =      13.429451 [THz] =     447.958282 [cm-1]
     freq (   18) =      13.429451 [THz] =     447.958282 [cm-1]
     freq (   19) =      13.517391 [THz] =     450.891613 [cm-1]
     freq (   20) =      13.517391 [THz] =     450.891613 [cm-1]
     freq (   21) =      13.517391 [THz] =     450.891613 [cm-1]
     freq (   22) =      15.038693 [THz] =     501.636816 [cm-1]
     freq (   23) =      15.038693 [THz] =     501.636816 [cm-1]
     freq (   24) =      15.038693 [THz] =     501.636816 [cm-1]
 **************************************************************************

     Mode symmetry, T_d (-43m)  point group:

     freq (  1 -  3) =        -43.5  [cm-1]   --> T_2  G_15 P_4   I+R
     freq (  4 -  6) =        144.5  [cm-1]   --> T_1  G_25 P_5      
     freq (  7 -  9) =        144.5  [cm-1]   --> T_2  G_15 P_4   I+R
     freq ( 10 - 10) =        401.3  [cm-1]   --> A_1  G_1  P_1   R  
     freq ( 11 - 12) =        401.3  [cm-1]   --> E    G_12 P_3   R  
     freq ( 13 - 15) =        401.4  [cm-1]   --> T_2  G_15 P_4   I+R
     freq ( 16 - 18) =        448.0  [cm-1]   --> T_1  G_25 P_5      
     freq ( 19 - 21) =        450.9  [cm-1]   --> T_2  G_15 P_4   I+R
     freq ( 22 - 24) =        501.6  [cm-1]   --> T_2  G_15 P_4   I+R

     PHONON       :  30m19.86s CPU  30m46.22s WALL

     INITIALIZATION: 
     phq_setup    :      0.05s CPU      0.05s WALL (       1 calls)
     phq_init     :     17.29s CPU     17.41s WALL (       1 calls)

     phq_init     :     17.29s CPU     17.41s WALL (       1 calls)
     set_drhoc    :      0.48s CPU      0.48s WALL (       3 calls)
     init_vloc    :      0.05s CPU      0.05s WALL (       1 calls)
     init_us_1    :      0.03s CPU      0.04s WALL (       1 calls)
     newd         :      0.03s CPU      0.05s WALL (       1 calls)
     dvanqq       :      2.28s CPU      2.28s WALL (       1 calls)
     drho         :     13.20s CPU     13.30s WALL (       1 calls)

     DYNAMICAL MATRIX:
     dynmat0      :      1.26s CPU      1.27s WALL (       1 calls)
     phqscf       :   1799.75s CPU   1821.86s WALL (       1 calls)
     dynmatrix    :      0.01s CPU      0.01s WALL (       1 calls)

     phqscf       :   1799.75s CPU   1821.86s WALL (       1 calls)
     solve_linter :   1795.50s CPU   1816.71s WALL (       9 calls)
     drhodv       :      4.22s CPU      4.30s WALL (       9 calls)

     dynmat0      :      1.26s CPU      1.27s WALL (       1 calls)
     dynmat_us    :      0.64s CPU      0.64s WALL (       1 calls)
     d2ionq       :      0.25s CPU      0.25s WALL (       1 calls)
     dynmatcc     :      0.37s CPU      0.37s WALL (       1 calls)

     dynmat_us    :      0.64s CPU      0.64s WALL (       1 calls)
     addusdynmat  :      0.00s CPU      0.00s WALL (       1 calls)

     phqscf       :   1799.75s CPU   1821.86s WALL (       1 calls)
     solve_linter :   1795.50s CPU   1816.71s WALL (       9 calls)

     solve_linter :   1795.50s CPU   1816.71s WALL (       9 calls)
     dvqpsi_us    :     27.41s CPU     27.54s WALL (     840 calls)
     ortho        :     36.05s CPU     36.20s WALL (    3780 calls)
     cgsolve      :   1239.36s CPU   1245.77s WALL (    3780 calls)
     incdrhoscf   :     75.59s CPU     76.56s WALL (    3780 calls)
     addusddens   :      5.67s CPU      5.68s WALL (      50 calls)
     vpsifft      :     53.03s CPU     53.84s WALL (    2940 calls)
     dv_of_drho   :      2.01s CPU      2.03s WALL (     108 calls)
     mix_pot      :      0.26s CPU      2.33s WALL (      41 calls)
     psymdvscf    :    319.97s CPU    322.27s WALL (      41 calls)
     newdq        :      8.59s CPU      8.60s WALL (      41 calls)
     adddvscf     :      5.84s CPU      5.85s WALL (    2940 calls)
     drhodvus     :      0.24s CPU      0.29s WALL (       9 calls)

     dvqpsi_us    :     27.41s CPU     27.54s WALL (     840 calls)
     dvqpsi_us_on :     11.39s CPU     11.40s WALL (     840 calls)

     cgsolve      :   1239.36s CPU   1245.77s WALL (    3780 calls)
     ch_psi       :   1214.82s CPU   1220.92s WALL (   61127 calls)

     ch_psi       :   1214.82s CPU   1220.92s WALL (   61127 calls)
     h_psi        :    987.99s CPU    993.34s WALL (   61127 calls)
     last         :    167.05s CPU    167.56s WALL (   61127 calls)

     h_psi        :    987.99s CPU    993.34s WALL (   61127 calls)
     add_vuspsi   :     62.42s CPU     62.65s WALL (   61127 calls)

     incdrhoscf   :     75.59s CPU     76.56s WALL (    3780 calls)
     addusdbec    :      9.29s CPU      9.32s WALL (    4620 calls)

     drhodvus     :      0.24s CPU      0.29s WALL (       9 calls)

      General routines
     calbec       :    191.60s CPU    192.28s WALL (  134364 calls)
     fft          :      3.81s CPU      3.99s WALL (    2595 calls)
     ffts         :      1.54s CPU      1.56s WALL (    1321 calls)
     fftw         :    933.18s CPU    939.55s WALL ( 1744776 calls)
     davcio       :      1.80s CPU      8.49s WALL (   13457 calls)
     write_rec    :      0.09s CPU      2.76s WALL (      50 calls)


     PHONON       :  30m19.86s CPU  30m46.22s WALL


   This run was terminated on:  12:44:49  26Jan2021            

=------------------------------------------------------------------------------=
   JOB DONE.
=------------------------------------------------------------------------------=
