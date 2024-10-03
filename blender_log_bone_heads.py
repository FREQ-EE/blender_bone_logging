import bpy
import csv
import os
from datetime import datetime

# Ensure the active object is an armature
armature = bpy.context.active_object
if armature.type != 'ARMATURE':
    print("Error: The active object is not an armature.")
    exit()

# Collect the world-space head positions of all bones in the armature
bone_heads = []
for bone in armature.pose.bones:
    # Convert bone head position to world space
    head_pos = armature.matrix_world @ bone.head
    bone_heads.append((bone.name, head_pos.x, head_pos.y, head_pos.z))

# Define the output directory and ensure it exists
output_dir = "FILE\PATH\HERE"
os.makedirs(output_dir, exist_ok=True)

# Define the output file name using ISO 8601 datetime
timestamp = datetime.now().isoformat(timespec='seconds').replace(":", "-")
output_file = os.path.join(output_dir, f"{timestamp}_bone_head_log.csv")

# Write the bone head positions to a CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Bone Name", "X", "Y", "Z"])  # Header row
    writer.writerows(bone_heads)

print(f"Bone head positions logged to '{output_file}'.")
