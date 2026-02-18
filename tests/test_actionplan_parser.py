import pytest

from hexi.core.schemas import ActionPlanError, parse_action_plan


def test_parse_action_plan_valid() -> None:
    raw = '{"summary":"do one thing","actions":[{"kind":"write","path":"a.txt","content":"x"}]}'
    plan = parse_action_plan(raw)
    assert plan.summary == "do one thing"
    assert plan.actions[0].kind == "write"


def test_parse_action_plan_rejects_extra_top_level_keys() -> None:
    raw = '{"summary":"x","actions":[{"kind":"read","path":"a"}],"oops":1}'
    with pytest.raises(ActionPlanError):
        parse_action_plan(raw)


def test_parse_action_plan_rejects_missing_emit_fields() -> None:
    raw = '{"summary":"x","actions":[{"kind":"emit","event_type":"progress"}]}'
    with pytest.raises(ActionPlanError):
        parse_action_plan(raw)
