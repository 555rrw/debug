# Cache-Read-Saver Skill

This directory contains the `cache-read-saver` skill, designed to optimize token usage for AI coding agents.

## Purpose
The `cache-read-saver` skill helps agents like Claude Code, Cursor, and others maintain high cache hit rates (cached input/read) during long sessions. By minimizing redundant codebase scans and model switching, it can reduce token costs by up to 90%.

## Key Features
- **Cache Optimization**: Strategies to keep context "warm" and reusable.
- **Workflow Efficiency**: Guidance on reading only necessary files and recording decisions.
- **Cost Reduction**: Specifically designed to lower the overhead of large repository analysis.
- **Session Continuity**: Integration with handoff processes for stable cross-session transitions.

## Usage
This skill is automatically triggered when Manus or other compatible agents identify a long-running coding task or large-scale repository modification where token efficiency is a priority.
