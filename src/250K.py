
import zutil


parameters = {

 # units for dimensional quantities
'units' : 'SI',

# reference state
'reference' : 'IC_1',

# restart from previous solution
'restart' : False,

'partitioner' : 'metis',

# time marching properties
'time marching' : {
                   'unsteady' : {
                                 'total time' : 1.0,
                                 'time step' : 1.0,
                                 'order' : 'second',
                                 'start' : 3000,
                                },
                   'scheme' : {
                               'name' : 'runge kutta',
                               'stage': 5,
                               'kind' : 'local timestepping',
                               },
                   # multigrid levels including fine mesh
                   'multigrid' : 4,
                   'cfl': 2.0,
                   'cycles' : 1000,
                  },

'equations' : 'euler',

'euler' : {
      'order' : 'second',
      'limiter' : 'vanalbada',
      'precondition' : True,
     },

'material' : 'air',

 "air": {
        "gamma": 1.4,
        "gas constant": 287.0,
        "Sutherlands const": 110.4,
        "Prandtl No": 0.72,
        "Turbulent Prandtl No": 0.9,
    },

'IC_1' : {
          'temperature':273.15,
          'pressure':101325.0,
          'V': {
                'vector' : [1.0,0.0,0.0],
                # Used to define velocity mag if specified
                'Mach' : 0.5,
                },
           #'viscosity' : 0.0,
           'Reynolds No' : 1.0e6,
           'Reference Length' : 1.0,
          'turbulence intensity': 0.01,
          'eddy viscosity ratio': 0.1,
          },
'IC_2' : {
          'reference' : 'IC_1',
          # total pressure/reference static pressure
          'total pressure ratio' : 1.0,
          # total temperature/reference static temperature
          'total temperature ratio' : 1.0,
          },
'IC_3' : {
          'reference' : 'IC_1',
          # static pressure/reference static pressure
          'static pressure ratio' : 1.0,
          },
'BC_1' : {
          'ref' : 7,
          'type' : 'symmetry',
         },
'BC_2' : {
          'ref' : 3,
          'type' : 'wall',
          'kind' : 'slip',
         },
'BC_3' : {
          'ref' : 9,
          'type' : 'farfield',
          'condition' : 'IC_1',
          'kind' : 'riemann',
         },
'BC_4' : {
          'ref' : 4,
          'type' : 'inflow',
          'kind' : 'default',
          'condition' : 'IC_2',
         },
'BC_5' : {
          'ref' : 5,
          'type' : 'outflow',
          'kind' : 'pressure',
          'condition' : 'IC_3',
         },
'write output' : {
                  'format' : 'vtk',
                  'surface variables': ['V','p','T','rho','cp'],
                  'volume variables': ['V','p','T','rho'],
                  'frequency' : 100,
                 },
'report' : {
            'frequency' : 10,
          },
}

############################
#
# Variable list
#
# var_1 to var_n
# p,pressure
# T, temperature
#
############################

