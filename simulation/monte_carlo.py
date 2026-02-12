import numpy as np
from config import CONFIG
from traffic_morphing.jitter import apply_jitter
from mixnet_sim.chain import run_mix_chain
from adversary_model.global_passive import GlobalPassiveAdversary
from cost_model.economic_model import AttackCostModel
from reporting.report import export_report

def run_monte_carlo():

    runs = CONFIG["runs"]
    n = CONFIG["sample_size"]
    jitter_max = CONFIG["jitter_max"]
    hops = CONFIG["mix_hops"]
    noise = CONFIG["observation_noise"]

    correlations = []
    adversary = GlobalPassiveAdversary(noise=noise)
    cost_model = AttackCostModel()

    for _ in range(runs):
        entry = np.linspace(0, 10, n)
        exit_times = apply_jitter(entry, jitter_max)
        exit_times = run_mix_chain(exit_times, hops)

        corr = adversary.correlate(entry, exit_times)
        correlations.append(corr)

    avg_corr = np.mean(correlations)
    cost = cost_model.estimate(n, avg_corr)

    print("Average Correlation:", avg_corr)
    print("Estimated Attack Cost:", cost)

    export_report(avg_corr, cost, runs, n)
