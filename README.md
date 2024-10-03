# Blender Bone Logging

## Overview
This script logs the world-space head positions of all bones in the active armature in Blender to a CSV file.

## Requirements
- Blender with an active armature object.

## Usage
1. Set the `output_dir` variable to your desired directory for the output CSV file.
2. Run the script in the Blender scripting editor.
3. A CSV file containing bone names and head positions (`X, Y, Z`) will be created in the specified directory.

## Notes
- The output filename includes a timestamp in ISO 8601 format.
- - Example output:
  ```csv
  Bone Name,X,Y,Z
  Bone_001,-2.7997015422442928e-05,2.7966068955720402e-05,29.338661193847656
  Bone_002,-0.00011005622945958748,0.00011153721425216645,29.224056243896484
  Bone_003,-0.0055082752369344234,0.005652317777276039,29.10971450805664
  Bone_004,-0.010906494222581387,0.01119309850037098,28.995372772216797
  ```
