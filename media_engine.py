# media_engine.py

def monitor(func):
    """Decorator to log start and completion of processing."""
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def play_count_stream(limit):
    """
    Generator that yields squared even numbers up to the limit.
    Ensures memory efficiency by not loading the entire list.
    """
    for i in range(limit):
        if i % 2 == 0:
            yield i**2

from media_engine import play_count_stream, monitor

# Setup from Appendix Instructions
SEED_NUM = 8
FAVORITE_ARTIST = "CUP OF JOE" # 12 characters
CONTROL_NUM = max(1, SEED_NUM)

# Mission Logic: Define limit
# limit = CONTROL_NUM + len(FAVORITE_ARTIST)
stream_limit = CONTROL_NUM + len(FAVORITE_ARTIST)

@monitor
def run_analytics(limit):
    total_plays = 0
    records_processed = 0
    generated_counts = []

    # Consuming the generator
    for count in play_count_stream(limit):
        generated_counts.append(count)
        total_plays += count
        records_processed += 1
    
    return total_plays, records_processed, generated_counts

# Execute
total, count, data_list = run_analytics(stream_limit)

# Assessment Data Output
print("-" * 30)
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"FAVORITE_ARTIST Used: {FAVORITE_ARTIST}")
print(f"Computed Stream Limit: {stream_limit}")
print(f"Generated Play Counts: {data_list}")
print(f"Total Plays: {total}")
print(f"Number of Records Processed: {count}")