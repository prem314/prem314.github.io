#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../../.." && pwd)"
thesis_cv_dir="$repo_root/thesis/post_doc/cv"
website_pdf="$script_dir/cv_prem.pdf"

"$thesis_cv_dir/cv_prem.sh"
cp "$thesis_cv_dir/cv_prem.pdf" "$website_pdf"
