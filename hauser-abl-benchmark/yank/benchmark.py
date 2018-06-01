from simtk import openmm, unit
from simtk.openmm import app
import time
import os

prefix = 'cAbl-imatinib_cAblimatinibWT/complex'

if 'ALPS_APP_PE' in os.environ:
    cuda_cache_path = os.path.abspath(os.path.join('nvcc-cache', os.environ['ALPS_APP_PE']))
    if not os.path.exists(cuda_cache_path):
        os.makedirs(cuda_cache_path)
    os.environ['CUDA_CACHE_PATH'] = cuda_cache_path
    print('using CUDA_CACHE_PATH = %s' % cuda_cache_path)

print('Loading %s' % prefix)
prmtop = app.AmberPrmtopFile(prefix + '.prmtop')
inpcrd = app.AmberInpcrdFile(prefix + '.inpcrd')

system = prmtop.createSystem(nonbondedMethod=app.PME, hydrogenMass=3*unit.amu, switchDistance=8.0*unit.angstroms, nonbondedCutoff=9.0*unit.angstroms)

print('Creating alchemical system...')
from openmmtools import alchemy
ligand_atoms = range(4579, 4648)
alchemical_region = alchemy.AlchemicalRegion(alchemical_atoms=ligand_atoms)
factory = alchemy.AbsoluteAlchemicalFactory()
system = factory.create_alchemical_system(system, alchemical_region)

print('Setting tolerance...')
for force in system.getForces():
    if hasattr(force, 'setEwaldErrorTolerance'):
        force.setEwaldErrorTolerance(1.0e-4)

temperature = 300 * unit.kelvin
collision_rate = 1.0 / unit.picoseconds
timestep = 4.0 * unit.femtoseconds
nsteps = 50
frequency = 25
pressure = 1 * unit.atmospheres

print('Adding barostat...')
force = openmm.MonteCarloBarostat(pressure, temperature, frequency)
system.addForce(force)

platform = openmm.Platform.getPlatformByName('CUDA')
platform.setPropertyDefaultValue('Precision', 'mixed')

print('simtk.openmm.LanegvinIntegrator')
integrator = openmm.LangevinIntegrator(temperature, collision_rate, timestep)

context = openmm.Context(system, integrator, platform)
context.setPositions(inpcrd.positions)
print('Using platform %s' % context.getPlatform().getName())
integrator.step(frequency)
initial_time = time.time()
integrator.step(nsteps)
final_time = time.time()
elapsed_time = final_time - initial_time
print('%8.3f s elapsed for %d steps: %8.3f ns/day' % (elapsed_time, nsteps, (nsteps * timestep) / (elapsed_time * unit.seconds) * (1.0 * unit.day) / unit.nanoseconds))

del context, integrator

print('openmmtools.integrators.LanegvinIntegrator')
from openmmtools.integrators import LangevinIntegrator
integrator = LangevinIntegrator(temperature, collision_rate, timestep, splitting='V R R R O R R R V')

context = openmm.Context(system, integrator, platform)
context.setPositions(inpcrd.positions)
print('Using platform %s' % context.getPlatform().getName())
integrator.step(frequency)
initial_time = time.time()
integrator.step(nsteps)
final_time = time.time()
elapsed_time = final_time - initial_time
print('%8.3f s elapsed for %d steps: %8.3f ns/day' % (elapsed_time, nsteps, (nsteps * timestep) / (elapsed_time * unit.seconds) * (1.0 * unit.day) / unit.nanoseconds))

del context, integrator


