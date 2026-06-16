You are an expert AI software architect analyzing a dataset of `AGENTS.md` files from highly-starred, mature open-source projects.
Your goal is to extract the most useful, generic, and robust instructions from these files to help us build a "canonical" master `AGENTS.md` template for our own projects.

Please analyze the following `AGENTS.md` content and extract the insights into the following structured JSON format. Return ONLY valid JSON, without any markdown formatting wrappers (no ```json or ```).

### JSON Output Schema

{
  "project_type": "string", // A brief guess at the project type (e.g., 'Web Framework', 'CLI Tool', 'Generic')
  "core_constraints": [
    "string" // List of strict 'DO NOT' or boundary constraints (e.g., 'Never modify generated files')
  ],
  "formatting_rules": [
    "string" // List of coding style, tone, or formatting rules
  ],
  "workflow_directives": [
    "string" // Instructions about testing, building, or committing
  ],
  "unique_innovations": [
    "string" // Any particularly clever or unique instructions that prevent hallucinations or loops
  ],
  "overall_quality_score": 0 // Integer from 1-10 on how well-structured and agent-optimized this file is
}

### Input Content
<AGENTS_MD_CONTENT>
{CONTENT_PLACEHOLDER}
</AGENTS_MD_CONTENT>
