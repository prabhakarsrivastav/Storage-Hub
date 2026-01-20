
import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Fix the middle section
# The exact string might vary slightly in whitespace, so let's be flexible or target the specific artifacts
# We know <!-- Trending Pendrive Section --> is unique.
# We want to remove the closing tags before it.
target_str = '<script src="script.js"></script>\n</body>\n\n</html><!-- Trending Pendrive Section -->'
replacement_str = '<!-- Trending Pendrive Section -->'

if target_str in content:
    content = content.replace(target_str, replacement_str)
else:
    # Try alternate spacing
    target_str_2 = '<script src="script.js"></script>\n</body>\n</html><!-- Trending Pendrive Section -->'
    if target_str_2 in content:
        content = content.replace(target_str_2, replacement_str)
    else:
        print("Could not find exact text to replace.")
        # Fallback: Find regex or just split
        parts = content.split('<!-- Trending Pendrive Section -->')
        if len(parts) > 1:
            # Look at the end of the first part
            # Remove <script...</html> from the end of parts[0]
            p0 = parts[0]
            # Simple heuristic: remove everything after last </div> and before end of string? 
            # Risk of removing too much.
            # Let's try to remove from the known script tag position
            idx = p0.rfind('<script src="script.js"></script>')
            if idx != -1:
                parts[0] = p0[:idx]
                content = parts[0] + '<!-- Trending Pendrive Section -->' + parts[1]

# Append the tags to the end if not present
if '</body>' not in content[-50:]:
    content += '\n    <script src="script.js"></script>\n</body>\n</html>'

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File fixed.")
