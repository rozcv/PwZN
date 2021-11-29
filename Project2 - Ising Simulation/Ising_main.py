import argparse
from rich.console import Console
from rich.progress import track
from Ising_simulation import simulationIsing
import time

parser = argparse.ArgumentParser(description="2D Ising model")
parser.add_argument('size', help='grating size', type=int)
parser.add_argument('J', help='J value', type=int)
parser.add_argument('B', help='B value', type=int)
parser.add_argument('H', help='H field value', type=int)
parser.add_argument('steps', help='Number of steps', type=int)
parser.add_argument('--density', help='Density of spins', default=0.5, type=float)
parser.add_argument('--file', help='Number of steps', default='step')
args = parser.parse_args()

console = Console()
console.clear()
console.rule("2D Ising simulation")

for i in track(range(10)):
    time.sleep(2)
    sim1 = simulationIsing(size=args.size, J=args.J, B=args.B,
                           H=args.H, steps=args.steps,
                           density=args.density, file=args.file)
    sim1.image()
