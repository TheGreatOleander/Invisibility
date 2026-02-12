# Anonymity Cost Amplifier  
### A Research Framework for Modeling Statistical Deanonymization Cost

---

## ⚠️ What This Is (And What It Is Not)

This is **not** a “perfect anonymity tool.”  
It is not magic.  
It does not claim to defeat a global passive adversary.

This repository exists for one purpose:

> To model anonymity as an economic and statistical arms race.

Anonymity is not binary.  
It is a gradient of cost.

This framework explores how traffic morphing, mixnets, noise, and identity isolation influence:

- Correlation strength  
- Required sample sizes  
- Statistical confidence  
- Computational cost  
- Economic feasibility of attack  

---

## Core Philosophy

Absolute anonymity is mathematically impossible against a true global observer with infinite samples.

However:

Deanonymization is not free.

If correlation requires:

- Massive sample accumulation  
- Significant compute  
- High-resolution timing capture  
- Expensive data retention  
- Complex statistical modeling  

Then anonymity becomes an **economic deterrent problem**, not a fantasy.

This project focuses on:

> Cost amplification over illusion.

---

## Design Principles

1. **Honesty Over Hype** – We do not promise the impossible.  
2. **Adversary Modeling First** – Security claims must be tested against defined threat models.  
3. **Statistical Rigor** – Results include confidence intervals and hypothesis testing.  
4. **Reproducibility** – Experiments are seed-controlled and CI-runnable.  
5. **Economic Framing** – We measure how expensive deanonymization becomes.  

---

## What This Framework Models

### Adversary Classes

Different observers have different powers:

- **Local adversary** – Partial network visibility  
- **Regional adversary** – Broader metadata access  
- **Global passive adversary** – Full network visibility with noise  

Each class can be extended and customized.

---

### Traffic Morphing

Simulated defenses include:

- Jitter injection  
- Packet delay shaping  
- Multi-hop mixnet batching  
- Exponential delay distributions  

Pluggable models may include:

- Poisson timing models  
- Bursty traffic distributions  
- Real-world trace replay  

---

### Mixnet Chains

Unlike low-latency anonymity systems, mixnets:

- Batch  
- Shuffle  
- Delay  
- Obfuscate timing signatures  

This repository models multi-hop mix chains and evaluates their effect on correlation decay.

---

### Monte Carlo Experiment Engine

Instead of single runs, we simulate:

- Dozens or hundreds of experiments  
- Randomized seeds  
- Statistical averaging  
- Distribution-level analysis  

Outputs include:

- Average correlation  
- Confidence intervals  
- Hypothesis test results  
- CSV exports for further analysis  

---

### Statistical Analysis Layer

We incorporate:

- t-tests against zero correlation  
- Confidence interval estimation  
- Reproducible seeding  
- Configurable significance thresholds (α)  

This moves the project from “simulation toy” into research territory.

---

### Economic Attack Cost Modeling

We translate correlation strength into estimated attack cost.

The model factors:

- Sample collection cost  
- Computational cost  
- Difficulty multiplier based on signal strength  

This reframes anonymity as:

> How expensive is it to break?

---

## Repository Structure

.
├── cli.py  
├── config.py  
├── simulation/  
├── adversary_model/  
├── traffic_morphing/  
├── mixnet_sim/  
├── statistics/  
├── cost_model/  
├── reporting/  
├── requirements.txt  
├── Dockerfile  
└── .github/workflows/ci.yml  

Each module is intentionally separated to support:

- Academic experimentation  
- Adversary swapping  
- Defense strategy comparison  
- Clean extension  

---

## Quick Start

Install dependencies:

    pip install -r requirements.txt

Run experiment:

    python cli.py

Or use Docker:

    docker build -t aca .
    docker run aca

---

## Example Output

Average Correlation: 0.0312  
Confidence Interval: (0.0121, 0.0498)  
p-value: 0.004  
Reject Null Hypothesis: True  
Estimated Attack Cost: 17654.23  
Results exported to experiment_results.csv  

Interpretation:

- Correlation is weak but non-zero  
- Statistically significant  
- Requires substantial sample accumulation  
- Attack cost amplified relative to baseline  

---

## What This Does NOT Guarantee

- It does not defeat a global passive adversary with infinite samples.  
- It does not claim information-theoretic anonymity.  
- It does not replace real-world operational security.  
- It does not prevent endpoint compromise.  

This is a research tool — not a silver bullet.

---

## Research Directions

Future expansions may include:

- Real traffic trace ingestion  
- Bayesian adversary models  
- Entropy pool modeling  
- Identity capsule lifecycle simulation  
- Multi-layer correlation modeling  
- GPU-based attack simulation  
- Whitepaper auto-generation  

---

## Intended Audience

- Privacy researchers  
- Network security engineers  
- Applied cryptography students  
- Anonymity system designers  
- Red/Blue team modelers  
- Graduate-level experimentation  

---

## Contribution Guidelines

1. Define your adversary model clearly.  
2. Provide statistical validation.  
3. Include reproducibility seed.  
4. Avoid marketing claims.  
5. Measure cost impact.  

Pull requests without empirical evidence will not be merged.

---

## License

MIT (or your preferred license)

---

## Final Word

Anonymity is not magic.

It is friction.

This repository is about increasing that friction  
until surveillance becomes economically irrational.

Welcome to the arms race.
