#!/bin/bash
# Clone every published Full Stack Skills package into a sibling workspace.

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
catalog_root="$(cd "$script_dir/.." && pwd)"
workspace_root="$(cd "$catalog_root/.." && pwd)"
target_dir="${FULL_STACK_SKILLS_REPOSITORIES_DIR:-$workspace_root/full-stack-skills-repositories}"
repository_list="$script_dir/repositories.txt"
organization="full-stack-skills"

mkdir -p "$target_dir"

while IFS= read -r repository; do
  if [[ -z "$repository" || "$repository" == \#* ]]; then
    continue
  fi
  destination="$target_dir/$repository"
  if [[ -d "$destination/.git" ]]; then
    echo "present  $repository"
    continue
  fi
  if [[ -e "$destination" ]]; then
    echo "ERROR: $destination exists but is not a Git repository" >&2
    exit 1
  fi
  echo "clone    $organization/$repository"
  git clone "https://github.com/$organization/$repository.git" "$destination"
done < "$repository_list"

echo "Repository inventory synchronized in $target_dir"
