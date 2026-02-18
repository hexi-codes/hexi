# Testing Strategy

Hexi tests prioritize contract and safety guarantees.

## Test layers

- schema and policy unit tests
- workspace/path traversal tests
- adapter request/response parsing tests
- orchestration behavior tests using fakes
- CLI behavior tests via Typer runner

## Why this mix

Core logic remains heavily unit-testable because side effects are isolated behind ports.

## Current focus areas

- allowlist enforcement,
- parser strictness,
- key resolution and onboarding flow,
- provider adapter error paths.
