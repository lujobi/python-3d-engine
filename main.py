from src.Engine import Engine
from src.app import App


WIDTH, HEIGHT = 1000, 1000

def run():
  e = Engine()
  app = App(WIDTH, HEIGHT, 'Test Engine', 30, e)
  app.run()

if __name__ == "__main__":
  run()