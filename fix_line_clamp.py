
import os

file_path = "styles.css"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if "-webkit-line-clamp: 2;" in line:
        # Check if next line already has line-clamp
        # We can't easily check the *next* line in this simple loop, but since we are iterating,
        # we can just blindly insert line-clamp: 2; if we want, OR better:
        # let's be smarter.
        pass

# Re-reading to do it properly with index
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# We want to replace "-webkit-line-clamp: 2;" with "-webkit-line-clamp: 2;\n    line-clamp: 2;"
# but only if line-clamp isn't already there.
# However, "line-clamp" is a substring of "-webkit-line-clamp", so simplistic replace is dangerous if not careful.
# But "-webkit-line-clamp: 2;" is specific.

search_str = "-webkit-line-clamp: 2;"
replace_str = "-webkit-line-clamp: 2;\n    line-clamp: 2;"

# We need to be careful not to double add if I partially added it before?
# No, the tool calls failed so the file should be unchanged regarding this.

# Let's do a line-by-line processing to be safe and keep indentation
final_lines = []
lines = content.splitlines()
for i, line in enumerate(lines):
    final_lines.append(line)
    if "-webkit-line-clamp: 2;" in line:
        # Check if next line mimics the current indentation + line-clamp
        # If the next line is NOT line-clamp, we add it.
        # But we need to be careful about not adding it if it's already there.
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if "line-clamp: 2;" in next_line and "-webkit-" not in next_line:
                continue

        # Get indentation
        indent = line[:line.find("-webkit")]
        final_lines.append(f"{indent}line-clamp: 2;")

with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(final_lines))

print("Fixed line-clamp compatibility.")
