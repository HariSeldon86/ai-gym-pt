# ai-gym-pt

A simple AI-powered personal trainer application that creates customized workout plans using large language models (LLMs) with structured output via LangChain 1.0.

**Project purpose:** generate reproducible, strongly-typed workout plans (the `Workout` model) from prompts by using LangChain's structured output parsing into `pydantic` models, then export results as JSON and TOON files.

**Status:** Prototype / demo

---

**What this repo does**
- Uses an LLM (configured by environment variables) via LangChain 1.0 to create workout plans.
- Produces a typed `Workout` object (declared in `models.py`) using a structured-output parser.
- Exports the produced `Workout` to both JSON and a simple `.toon` format for downstream use.

---

**Quick Start (Windows PowerShell)**

1. Install dependencies using `uv`:

```powershell
uv sync --locked
```

2. Configure your LLM credentials via a .env file

- Rename the example `.env.example` to `.env` and populate it with your API key.
- Ensure `.env` is ignored by git.

3. Run the demo:

```powershell
uv run main.py
```

---

**Files & responsibilities**
- `main.py`: Entrypoint and demo runner.
	- Invokes the LLM through LangChain 1.0 and the configured structured output parser to create a `Workout` object.
	- Performs any local post-processing and writes the produced object to `JSON` and `TOON` files (example exports: `example_workout_plan.json`, `example_workout_plan.toon`).
- `models.py`: Contains the `pydantic` models for the structured `Workout` output and any nested submodels (exercises, sets, metadata).
- `data_models.py`: Defines the smaller data field models used within `Workout`.
- `example_workout_plan.json` / `example_workout_plan.toon`: Example exports created by `main.py` to illustrate the output formats.
- `uv.lock` / `pyproject.toml`: Dependency metadata and installation manifest.

---

**How structured output works (overview)**
- `models.py` declares a `Workout` `pydantic` model.
- `main.py` uses LangChain's output-parsing tools so the raw LLM text is validated and parsed into the `Workout` object.
- That `Workout` object is fully typed so downstream code (exporters, UI, analyzers) can depend on field names and types safely.


---

**Configuration & environment variables**
- `OPENAI_API_KEY` (or provider-specific keys): credential for the chosen LLM provider.

If you add additional providers, update `main.py` accordingly to support different LangChain LLM wrappers.

---

**Development notes**
- Target LangChain: `1.0.x` — pin with `pip install "langchain>=1.0,<2.0"`.
- Models: `pydantic` is used for typed validation and (optionally) for generating the prompt schema via an output parser.
- Exports: JSON is canonical; `.toon` is a lightweight illustrative format used in this repo. See `main.py` for exact serialization logic.

---

**License & contact**
This repository is provided as-is for demo and educational purposes and under MIT LICENCE.
