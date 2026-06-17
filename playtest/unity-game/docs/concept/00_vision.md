# Lumen (working title)

A cozy little game about a lighthouse keeper's lantern that has to relight the
stars. Calm, hand-drawn, melancholic but warm. 2D, side-on, exploration plus
gentle light puzzles. No combat, no fail state, you can't die, you just wander and
solve quiet things.

Building it in Unity (the team knows C#, and I want the animation and asset
tooling). PC first via Steam, and I would love Switch later, so keep an eye on
perf and abstract the input early. 60fps is non-negotiable, it has to feel
buttery.

Art is the whole point: a muted nordic palette, cool tones, soft glows, lots of
negative space, parallax depth. The lantern light is the one warm accent in a cold
world. Hand-painted backgrounds and skeletal 2D animation.

Things I care about: playtests need to be reproducible, so keep gameplay
deterministic where we can. Save anywhere. No microtransactions, ever. We use the
Unity Test Framework for the puzzle and inventory logic, and CI must be able to
build a player headlessly. Audio is huge (adaptive music), probably FMOD later.

Hard rules from painful experience: never hand-edit the .meta files, and never
resolve a scene or prefab merge conflict blind, scenes are basically binary to us.
