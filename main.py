from access_control import compute_access_level, validate_access

SEED_NUM = 8  
FAVORITE_ARTIST = "CUP OF JOE" 
CONTROL_NUM = max(1, SEED_NUM)

level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
decision = validate_access(level, CONTROL_NUM)

print("-" * 30)
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"FAVORITE_ARTIST Length: {len(FAVORITE_ARTIST)}")
print(f"Computed Access Level: {level}")
print(f"Threshold Applied: {CONTROL_NUM * 5}")
print(f"Final Authorization Decision: {decision}")
