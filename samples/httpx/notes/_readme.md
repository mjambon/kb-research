# Navigate and maintain the committed source knowledge base

The source root contains one registered Git repository, `/github/encode/httpx/`, under the organizational folders `/github/` and `/github/encode/`. All 125 tracked Git blobs at commit `ca097c96f97d8d2a5da09b8ca736c7e78a2467f6` and all 20 source folders have regular Markdown ghosts at the same relative paths under `notes/`. There are no committed symlinks or submodules at this revision. The workspace link that exposes the repository under `src/` is a setup link, not a committed source object.

## Architecture and navigation

HTTPX exports one-shot helpers and persistent sync/async clients from `/github/encode/httpx/httpx/`. Client policy merges configuration and drives auth, redirects, hooks, and transport selection; request/response models handle headers, cookies, bodies, and decoding. Default transports adapt to httpcore, while ASGI, WSGI, and mock transports support in-process requests. `/github/encode/httpx/tests/` checks these contracts; `/github/encode/httpx/docs/` explains user behavior; `/github/encode/httpx/scripts/` and `/github/encode/httpx/.github/` maintain builds and releases.

## Maintenance conventions

Every source identifier is rooted at `src/` and written with a leading slash, such as `/github/encode/httpx/httpx/_client.py`; folder references end in `/`. Symbol names beside paths disambiguate behavior. Read committed Git objects at the pinned revision, not working-tree files, before updating a ghost. If the checkout becomes dirty, report it and continue from the captured commit. Keep historical release claims in the changelog ghost distinct from current behavior. Update folder summaries after file-level changes. The repository root ghost baseline certifies completion only at its stated commit.

Useful investigation paths: read `/github/encode/httpx/pyproject.toml` for packaging and pytest settings; trace public exports through `/github/encode/httpx/httpx/__init__.py`; follow `Client.send` and `AsyncClient.send` to transport `handle_request` methods; inspect paired tests in `/github/encode/httpx/tests/client/`, `/github/encode/httpx/tests/models/`, and `/github/encode/httpx/tests/`. For assets, search committed text blobs for the basename and inspect the built site if publication behavior matters. Git `ls-tree -rz --full-tree <commit>` is the inventory source; Git `cat-file blob <object>` supplies exact content.

## Tag definitions

Tags apply to every relevant ghost in the whole source tree unless the definition narrows scope. They cover implementations, focused tests, guides, and folder overviews when the topic is central; incidental mentions do not qualify.

- `api`: defines, tests, or documents caller-facing Python behavior or types.
- `asset`: tracked binary documentation material and its containing folder.
- `async`: implements, tests, or documents an asynchronous request or transport contract.
- `auth`: implements, tests, or documents credential or authentication flows.
- `build`: controls packaging, CI, development commands, or publication.
- `cli`: implements or tests the optional command-line interface.
- `community`: configures GitHub contribution and issue interactions.
- `config`: defines, tests, or documents runtime or developer configuration inputs.
- `docs`: content or assets published on the documentation site, plus source README and changelog.
- `error`: defines, maps, tests, or documents exception behavior.
- `legal`: states redistribution terms.
- `request`: constructs, transforms, sends, tests, or documents request data.
- `response`: interprets, classifies, tests, or documents response data.
- `security`: handles credentials, TLS, origin/URL validation, sensitive headers, or related boundary tests and guidance.
- `streaming`: implements or tests byte-stream production, consumption, or decoding.
- `testing`: test code, fixtures, or test execution controls.
- `transport`: defines, routes, tests, or documents the I/O boundary and implementations.
- `url`: parses, stores, normalizes, matches, tests, or documents URLs and query parameters.

## Coverage and limits

Coverage is for committed revision `ca097c96f97d8d2a5da09b8ca736c7e78a2467f6` of the one identified Git repository. The source checkout was clean when captured and detached. No external consumers, deployed documentation state, or live third-party integration behavior was verified; their documentation entries are navigation pointers. The notes mirror committed evidence and do not claim a newer checkout revision.
