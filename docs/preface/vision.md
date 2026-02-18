# Vision

Hexi exists to make coding agents **boring in the best way**: inspectable, bounded, and replaceable.

## The gap Hexi targets

Many agent tools are either:
- too minimal to operationalize, or
- too heavy to trust quickly.

Hexi sits in the middle: strong execution boundaries with a small code footprint.

## Product thesis

- Treat model output as **data contracts**, not prose.
- Keep orchestration in a tiny core service.
- Push side effects to adapters behind ports.
- Make the runlog the source of operational truth.

## Design constraints for v0.1.0

- Single-step loop only.
- Local git repo only.
- No background workers.
- No database.
- No plugin registry.

These constraints are deliberate. They keep refactors cheap and behavior legible.

## Long-term direction

Hexi can expand in layers without breaking contracts:
- richer policy checks,
- stronger review artifacts,
- more model adapters,
- optional persistence upgrades.

The core contract should remain stable as internals evolve.
