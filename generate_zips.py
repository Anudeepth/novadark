import os
import zipfile
import json
import uuid

STAGES = [
    {"id": 1, "name": "Stage 1", "clue": "The first step into the dark is listening to what remains unsaid."},
    {"id": 2, "name": "Stage 2", "clue": "Radio static at 104.7 MHz reveals patterns if you invert the wave."},
    {"id": 3, "name": "Stage 3", "clue": "Every archive contains a deleted entry. Look behind index 03."},
    {"id": 4, "name": "Stage 4", "clue": "Zeroes and ones are just light turned off and on."},
    {"id": 5, "name": "Stage 5", "clue": "The basement holds more than cold water pipes."},
    {"id": 6, "name": "Stage 6", "clue": "A sound repeated seven times changes its origin."},
    {"id": 7, "name": "Stage 7", "clue": "The shift is not by three, but by the hour of night."},
    {"id": 8, "name": "Stage 8", "clue": "Moving objects leave trails in the phosphor layer."},
    {"id": 9, "name": "Stage 9", "clue": "Transmission sent from an unlisted terminal."},
    {"id": 10, "name": "Stage 10", "clue": "Silence has a frequency if you listen deep enough."},
    {"id": 11, "name": "Stage 11", "clue": "Do not follow straight corridors; turn where the light flickers."},
    {"id": 12, "name": "Stage 12", "clue": "The tape ends before the sentence is completed."},
    {"id": 13, "name": "Stage 13", "clue": "Unfinished things are kept in repositories. Check the versions left behind."},
    {"id": 14, "name": "Final", "clue": "The moon doesn't keep secrets, but it reflects them. You have reached the final horizon."}
]

os.makedirs("downloads", exist_ok=True)

# Remove any old stage_15.zip if it exists
old_stage_15 = os.path.join("downloads", "stage_15.zip")
if os.path.exists(old_stage_15):
    os.remove(old_stage_15)
    print(f"Removed deprecated: {old_stage_15}")

for stage in STAGES:
    num = f"{stage['id']:02d}"
    zip_filename = f"stage_{num}.zip"
    zip_path = os.path.join("downloads", zip_filename)
    
    intel_content = f"""========================================
NOVA AFTER DARK :: STAGE {num}
Codename: {stage['name']}
========================================

INTEL LOG:
{stage['clue']}

TIMESTAMP: 2026-09-27T03:00:{num}+00:00
STATUS: UNVERIFIED
ORIGIN: SECTOR-{num}-DARK
"""
    meta_content = json.dumps({
        "stage": stage["id"],
        "code": f"STAGE_{num}",
        "name": stage["name"],
        "verified": True,
        "checksum": uuid.uuid4().hex
    }, indent=2)

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f"stage_{num}_intel.txt", intel_content)
        zf.writestr("metadata.json", meta_content)
        
    print(f"Generated: {zip_path} ({os.path.getsize(zip_path)} bytes)")

print("All 14 stage zip files generated successfully.")
