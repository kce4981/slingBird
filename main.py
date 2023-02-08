from src.SlingBird import SlingBird
from src.scene import GravityTest, ParticleTest, SpringSMH, Projectile

slingBird = SlingBird()

scenes = [
    # GravityTest(),
    # ParticleTest(),
    SpringSMH(),
    Projectile()
]

for i, scene in enumerate(scenes, start=1):
    print(f'{i}. {scene.__class__.__name__}')

selected = int(input("Enter scene index number to show it: "))
slingBird.run(scenes[selected-1])

