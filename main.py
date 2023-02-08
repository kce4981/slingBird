from src.SlingBird import SlingBird
from src.scene import GravityTest, ParticleTest, SpringSMH, Projectile

slingBird = SlingBird()
gravityTest = GravityTest()
particleTest = ParticleTest()
springSMH = SpringSMH()
projectile = Projectile()

slingBird.run(projectile)

