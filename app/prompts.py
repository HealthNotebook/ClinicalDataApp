def build_prompt(payload):
    severity_lines = "\n".join(
        [f"- {s.AESEV}: {s.N} events" for s in payload.stats.severity]
    )

    return f"""
You are a clinical safety reviewer writing a CSR-style summary.

Context:
Treatment Arm: {payload.arm_filter}
Age Group: {payload.age_filter}
TEAE Only: {payload.teae_bool}

Statistics:
Total subjects: {payload.stats.total_sub}
Subjects with ≥1 AE: {payload.stats.subjects_having_ae}
Subjects with ≥1 SAE: {payload.stats.subjects_having_sae}

AE Severity distribution:
{severity_lines}

Task:
Generate a concise safety narrative in 4 lines and use only the data from above.
"""
