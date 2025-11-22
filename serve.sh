#!/usr/bin/env bash
set -euo pipefail

# Run the site locally with the project-local Ruby gems to avoid system installs.

ROOT="$(cd "$(dirname "$0")" && pwd)"

export HOME="$ROOT/.home"
export XDG_DATA_HOME="$HOME/.local/share"
export GEM_HOME="$ROOT/.gems"
export GEM_PATH="$GEM_HOME"
export GEM_SPEC_CACHE="$GEM_HOME/specs"
export PATH="$GEM_HOME/bin:$PATH"

mkdir -p "$HOME/.local/share"

exec bundle exec jekyll serve --livereload "$@"
