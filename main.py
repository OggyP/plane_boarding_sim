from planeSimHeadless import Plane_Simulation as HeadlessSim
from planeSim import Plane_Simulation as VisualSim
# import asyncio

# ticks_taken = []

# async def run_function():
#     sim = HeadlessSim()
#     while sim.running:
#         sim.tick()
#     ticks_taken.append(sim.current_tick)

# async def main():
#     simulations = []
#     for i in range(100):
#         simulations.append(asyncio.create_task(run_function()))

#     for sim in simulations:
#         try:
#             await sim
#         except asyncio.CancelledError:
#             pass

# asyncio.run(main())

sim = VisualSim(5)