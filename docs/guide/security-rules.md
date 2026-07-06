# Harmonic Coding Security Rules

> Security rules that should be treated as first-class workflow inputs during setup, implementation, and review.

Use these rules in:

- security review
- PR review when auth, secrets, or external input handling changed
- setup and CI/CD decisions that affect secret storage or execution trust

## Core rule

Prefer a small number of concrete, reusable security rules over a large generic checklist.

## Required checks

### 1. Secrets and credentials

- do not commit secrets, tokens, or private credentials
- do not place live secret values in docs or examples
- document where secrets come from without exposing them

### 2. Auth and session handling

- treat auth boundaries as explicit review surfaces
- require review when login, session, token, role, or access checks change
- do not assume a working happy path means the authorization model is correct

### 3. Input handling and injection risk

- review new input surfaces
- require validation boundaries to be clear
- treat query construction, shell invocation, template rendering, and external calls as injection-sensitive

### 4. Unsafe comparisons and identity checks

- call out fragile equality checks when they protect sensitive decisions
- document the expected safe comparison pattern for the target stack

### 5. Logging and error exposure

- logs must not leak secrets or sensitive user material
- operator-facing errors should be informative without exposing internal details that widen risk

### 6. CI and workflow security

- review workflow changes that affect permissions, branch trust, secrets use, or untrusted input execution
- do not treat automation files as low-risk just because they are not application code

## Severity framing

Use these levels when reporting security findings:

- **Critical** — likely compromise or major unsafe exposure
- **High** — meaningful exploit path or broken trust boundary
- **Medium** — real weakness that should be fixed before confidence is high
- **Low** — minor issue or follow-up hardening item

## How to use these rules

1. identify the real security surface
2. review only the relevant rules
3. report concrete risk and required action
4. avoid noisy generic warnings
