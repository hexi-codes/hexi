# todo_refiner

Tiny wrapper project that uses Hexi CLI as the execution engine.

## Setup
```bash
pip install -e ../..
cp .env.example .env  # optional
```

## Run
```bash
python run.py "Refactor TODO comments into issue references"
```

The script calls:
```bash
hexi run "<task>"
```
