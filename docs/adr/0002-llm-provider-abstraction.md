# ADR 0002: LLM Provider Abstraction

## Status

Proposed

## Context

The system uses an LLM for tasks such as understanding customer requests,
analyzing retrieved supplier data, and generating structured outputs.

The application should not depend directly on a specific LLM provider such as Anthropic.

Different deployment environments may require different LLM providers.
For example, some organizations may use a hosted provider such as Anthropic,
while others may require a self-hosted or internal model due to security,
privacy, compliance, or infrastructure requirements.

Agents should therefore depend on an LLM abstraction rather than directly
on a provider-specific implementation.

## Decision

The application will define an `LLMClient` abstraction that represents
the capabilities required by agents to interact with a Large Language Model.

Agents will depend only on the `LLMClient` abstraction and will not depend
directly on Anthropic or any other LLM provider.

Provider-specific implementations will be placed in the infrastructure layer.

The initial implementation will be `AnthropicLLMClient`, which will use
the Anthropic API to communicate with Claude.

The concrete LLM provider will be selected and configured in the application
composition root using dependency injection.

This design allows additional providers, including self-hosted or internal
LLMs, to be introduced without changing agent business workflows.

## Alternatives

### 1. Direct dependency on Anthropic

Agents could depend directly on `AnthropicLLMClient`.

This would be simpler initially, but it would tightly couple application
logic to a specific provider and make future provider replacement more difficult.

### 2. Provider-specific agents

Separate agents could be implemented for each LLM provider, for example
`AnthropicResearchAgent` or `LocalResearchAgent`.

This would duplicate agent workflow logic and mix provider integration
concerns with application-level responsibilities.

### 3. LLM provider abstraction

Agents depend on a common `LLMClient` abstraction while provider-specific
implementations are isolated in the infrastructure layer.

This option was selected because it keeps agent workflows independent
from the underlying LLM provider.

## Consequences

### Positive

- Agents are decoupled from a specific LLM provider.
- LLM providers can be replaced without changing agent workflow logic.
- Provider-specific SDKs and API details remain isolated in the infrastructure layer.
- Self-hosted or internal company models can be introduced in the future.
- Agents can be tested using a fake or mock `LLMClient` without making real API calls.
- Provider selection can be controlled through application configuration and dependency injection.

### Negative

- The abstraction introduces an additional interface and infrastructure layer.
- Different LLM providers may expose different capabilities, making a completely universal abstraction difficult.
- Provider-specific features may require extensions to the common interface.
- Supporting multiple providers increases integration and testing complexity.