# GitHub Copilot Instructions for Mérida Tech Week Workshop

## Project Overview

This is an **educational repository** for teaching GitHub Copilot to university students at Tec de Mérida. It contains structured workshop materials, code examples, and practice guides designed for students with basic Python and web development knowledge.

**Target Audience:** Students learning AI-assisted development  
**Languages:** Spanish (documentation), Python, HTML/CSS/JavaScript (code)

## Architecture & Structure

```
merida-tech-week-copilot-workshop/
├── examples/          # Starter code with TODOs for students
├── solutions/         # Reference implementations (instructor use)
├── materials/         # Practice guides (Practica-1.md, Practica-2.md, etc.)
├── resources/         # Prompt libraries and student resources
└── assets/videos/     # Demo GIF for README
```

**Key Pattern:** `examples/` files contain `TODO` comments for students to complete with Copilot. Corresponding `solutions/` files show expected outcomes.

## Developer Workflows

### Running Python Examples
```bash
# No dependencies needed - uses Python stdlib only
python examples/01_generate_code.py
python -m unittest examples/03_unit_tests_example.py
```

### Testing Student Progress
Compare student work in `examples/` against reference `solutions/` files.

## Project Conventions

### 1. Documentation Language
- All markdown documentation is in **Spanish** with professional but approachable tone
- Code comments and docstrings are in **Spanish**
- Prompts examples use **English** (as that's what Copilot expects)

### 2. Code Style for Examples
- **Python:** Type hints required (`typing.List`, return types), Spanish docstrings using `:param:` style
- **Error Handling:** Explicit `ValueError` with Spanish messages for invalid inputs (see `solutions/01_generate_code_solution.py`)
- **Naming:** Descriptive Spanish function names (`promedio_lista`, `maximo_lista`)

Example from `solutions/01_generate_code_solution.py`:
```python
def promedio_lista(numeros: List[float]) -> float:
    """
    Calcula el promedio de una lista de números.
    
    :param numeros: Lista de valores numéricos.
    :return: Promedio de los valores de la lista.
    :raises ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return sum(numeros) / len(numeros)
```

### 3. TODO Pattern for Student Exercises
Mark incomplete sections with descriptive TODO comments in Spanish:
```python
# TODO: Usa GitHub Copilot para generar una función que calcule el promedio
# de una lista de números. La función debe llamarse "promedio_lista" y
# debe manejar el caso de lista vacía lanzando un ValueError.
```

### 4. Prompt Documentation Format
When documenting prompts for students (`resources/awesome_prompts.md`):
- Organize by task category (Generation, Refactoring, Testing)
- Show exact English prompt strings in blockquotes
- Include context about when to use each prompt

### 5. Practice Structure
Each practice guide (`materials/Practica-X.md`) follows this pattern:
1. 🎯 Objective statement
2. Step-by-step instructions with file references
3. Specific Copilot prompts to use
4. Expected outcomes

## Critical Integration Points

### Web Practices (Practica-2)
- Uses **ChatGPT for content generation** + **Copilot for code generation**
- Final deliverable: Portfolio published to GitHub Pages
- No build tools - pure HTML/CSS/JS for simplicity

### Python Practices (Practica-1)
- Zero external dependencies (no requirements.txt)
- Focuses on Copilot inline suggestions + Chat + Edit modes
- Testing with stdlib `unittest` only

## When Generating Content

**For Educational Materials:**
- Use emojis for section headers (🎯, 📁, ✅, 💬)
- Keep tone encouraging and practical
- Include "why" explanations, not just "how"
- Reference specific files by name (e.g., `examples/01_generate_code.py`)

**For Code Examples:**
- Always include docstrings in Spanish
- Handle empty list edge cases with `ValueError`
- Type hints are non-negotiable
- Show both "before" (with TODO) and "after" (in solutions/) versions

**For Prompts:**
- Write in English (Copilot's native language)
- Be specific about output format (e.g., "add Spanish docstrings")
- Include context ("this function", "this file")

## Avoid

- ❌ Adding npm/pip dependencies (keep it simple)
- ❌ English-language student-facing docs
- ❌ Generic programming advice without codebase examples
- ❌ Complex build processes or tooling
- ❌ Referencing files that don't exist in the actual structure

## Testing Your Changes

Before committing educational materials:
1. Verify file paths in practice guides point to actual files
2. Test that Python examples run without dependencies: `python examples/*.py`
3. Ensure Spanish documentation is clear and grammatically correct
4. Check that prompts in `resources/` match actual Copilot usage patterns
