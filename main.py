import os

# Entry must stay within the 200-character limit.
line = (
    "It's you from 2046. Do NOT buy the blue mug tomorrow - "
    "it chips on day one and I still think about it every morning. "
    "The house fire in 2031? We rebuilt. The mug haunts me."
)
assert len(line) <= 200

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
