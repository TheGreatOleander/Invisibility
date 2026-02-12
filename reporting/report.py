from datetime import datetime

def export_report(avg_corr, cost, runs, samples):

    content = f"""
# Experiment Report

Date: {datetime.utcnow()}

Runs: {runs}
Samples per Run: {samples}

Average Correlation: {avg_corr}
Estimated Attack Cost: {cost}
"""

    with open("experiment_report.md", "w") as f:
        f.write(content)

    print("Report exported to experiment_report.md")
