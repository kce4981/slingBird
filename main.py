from src.SlingBird import SlingBird
from src.scene import GravityTest, ParticleTest, SpringSMH

slingBird = SlingBird()
gravityTest = GravityTest()
particleTest = ParticleTest()
springSMH = SpringSMH()


slingBird.run(springSMH)

