from src.Engine import Engine
from src.app import App
import numpy as np

WIDTH, HEIGHT = 1000, 1000

def run():
  e = Engine(WIDTH, HEIGHT)
  app = App(WIDTH, HEIGHT, 'Test Engine', 30, e)
  app.run()

if __name__ == "__main__":
  run()