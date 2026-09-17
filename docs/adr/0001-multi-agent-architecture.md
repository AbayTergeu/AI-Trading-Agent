# ADR-001: Multi-Agent Architecture

## Status

Proposed

## Context

The system needs to perform a multi-step procurement workflow that includes lead research, supplier discovery, supplier evaluation, and quotation preparation.

A single LLM agent would have too many responsibilities and would receive unnecessary context. We therefore need a multi-agent architecture where specialized agents perform focused tasks and an orchestrator coordinates the overall workflow.

## Decision

We will use an orchestrator-based multi-agent architecture.

A central orchestrator will coordinate specialized agents, each responsible for a focused part of the procurement workflow.

Initial agents will include:

- Research Agent - researches customer and product information.
- Supplier Research Agent - finds and collects potential supplier information.
- Quotation Agent - prepares a customer quotation from validated sourcing data.

Agents will interact through explicit, structured inputs and outputs rather than sharing the entire conversation context.

The orchestrator will control the workflow, retries, validation gates, and transitions between agents.

External capabilities such as web search, LLM providers, databases, and other services will be accessed through tools or application interfaces rather than directly embedded into domain logic.

## Consequences

### Positive

- Each agent has a focused responsibility, making the system easier to understand and test.
- The orchestrator provides explicit control over workflow state, sequencing, retries, and validation.
- Agents receive only the context required for their task, reducing unnecessary context growth.
- Individual agents can be improved or replaced without redesigning the entire workflow.
- Validation gates can be applied between workflow steps.
- Failures can be isolated and handled without losing the entire workflow state.

### Negative

- The system is more complex than a single-agent architecture.
- The orchestrator becomes an important component that must be carefully designed and tested.
- Communication between agents requires explicit contracts and state management.
- Multiple LLM calls can increase latency and token costs.
- Distributed failures and retries require additional observability and idempotency mechanisms.