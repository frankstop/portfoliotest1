#!/bin/sh
set -eu

repo='frankstop/portfoliotest1'
description='Frank Valdez’s portfolio: selected projects, interactive experiments, and a little fun. Built with HTML, CSS, and JS.'

gh api "repos/$repo" --silent
gh api --method PATCH "repos/$repo" \
  -f description="$description" \
  -f homepage='https://frankiejvaldez.com/portfoliotest1/' --silent

# Reuse an existing Pages site; create one only when GitHub confirms it is absent.
if result=$(gh api "repos/$repo/pages" 2>&1); then
  gh api --method PUT "repos/$repo/pages" -f build_type=workflow --silent
else
  case "$result" in
    *'HTTP 404'*)
      gh api --method POST "repos/$repo/pages" -f build_type=workflow --silent
      ;;
    *) printf '%s\n' "$result" >&2; exit 1 ;;
  esac
fi

printf '%s\n' 'Repository description and Pages settings updated.' \
  'Push the included files to the default branch, or run Deploy portfolio in Actions.'
