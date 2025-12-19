import sys
import json
import re


def process_content(content):
    def replace_circuit(match):
        json_path = match.group(1).strip()
        circuit_id = f"circuit-{hash(json_path) % 10000}"

        return f"""
  <div id="{circuit_id}"></div>
  <script>
    (function() {{
      fetch('{json_path}')
        .then(r => r.json())
        .then(data => {{
          const circuit = new digitaljs.Circuit(data);
          const paper = circuit.displayOn($('#{circuit_id}'));
        }})
        .catch(err => console.error('Failed to load circuit:', err));
    }})();
  </script>
"""

    return re.sub(r"\{\{#circuit\s+(.+?)\}\}", replace_circuit, content)


def main():
    if len(sys.argv) > 1:
        supports = sys.argv[1]
        renderer = sys.argv[2]
        if supports == "supports":
            print(f"{sys.argv[0]} invoked using {renderer}")
            sys.exit(0)  # support all renderers
        else:
            sys.exit(1)

    # we've been invoked a second time by mdbook
    context, book = json.load(sys.stdin)
    chapters = [c["Chapter"] for c in book["items"]]
    for chapter in chapters:
        chapter["content"] = process_content(chapter["content"])
    json.dump(book, sys.stdout)


if __name__ == "__main__":
    main()
