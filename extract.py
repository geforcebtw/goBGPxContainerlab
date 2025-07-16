import json

# Charging the file
file = "extract.json" # Edit as needed

with open(file, "r") as f:
    rib = json.load(f)
print("\n")
print("*" * 40)
print(" " *10 + "EXTRACTION DU JSON")
print("*" * 40)
print("\n")

# RIB browse
for prefix, paths in rib.items():
    for path in paths:
        nexthop = None
        as_path = []
        for attr in path.get("attrs", []):
            if attr["type"] == 3:
                nexthop = attr.get("nexthop")
            elif attr["type"] == 2:
                # attr["as_paths"] list of segments
                for segment in attr["as_paths"]:
                    as_path.extend(segment.get("asns", []))  # if present

        neighbor = path.get("neighbor-ip")

        # Print in the terminal      
        print(f"Prefix: {prefix}")
        print(f"  Nexthop: {nexthop}")
        print(f"  Neighbor: {neighbor}")
        print(f"  AS Path: {' '.join(map(str, as_path)) if as_path else '(empty)'}")
        print("-" * 40)
