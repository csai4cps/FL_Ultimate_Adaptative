import yaml
from src.experiments.benchmark import FederatedBenchmark

if __name__ == "__main__":
    with open("configs/sybil_attack.yaml") as f:
        config = yaml.safe_load(f)

    exp = FederatedBenchmark(config)
    exp.run()
