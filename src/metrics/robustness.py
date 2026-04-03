def attack_success_rate(predictions, target_label):
    return (predictions == target_label).mean()
