from planeSimHeadless import Plane_Simulation as HeadlessSim
from planeSim import Plane_Simulation as VisualSim
# import asyncio

# ticks_taken = []

# async def run_function(i):
#     sim = HeadlessSim()
#     while sim.running:
#         sim.tick()
#     ticks_taken.append(sim.current_tick)
#     print("Done Simulation " + str(i))

# async def main():
#     simulations = []
#     for i in  range(100):
#         simulations.append(asyncio.create_task(run_function(i)))

#     for sim in simulations:
#         try:
#             await sim
#         except asyncio.CancelledError:
#             pass

#     print(ticks_taken)

# asyncio.run(main())

sim = VisualSim(15)