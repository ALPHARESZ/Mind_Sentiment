LABEL_SCORE = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

def calculate_negative_streak(labels):

    max_streak = 0
    current = 0

    for label in labels:

        if label == "negative":

            current += 1

            max_streak = max(
                max_streak,
                current
            )

        else:

            current = 0

    return max_streak


def calculate_volatility(labels):

    switches = 0

    for i in range(1, len(labels)):

        if labels[i] != labels[i - 1]:

            switches += 1

    return switches


def calculate_recovery(labels):

    recovery = 0

    for i in range(1, len(labels)):

        prev_label = labels[i - 1]

        current_label = labels[i]

        if (
            prev_label == "negative"
            and current_label == "positive"
        ):

            recovery += 1

    return recovery


def calculate_recent_trend(labels):

    weights = [1, 2, 3, 4, 5, 6, 7]

    score = 0

    for label, weight in zip(labels, weights):

        score += (
            LABEL_SCORE[label] * weight
        )

    return score


def analyze_burnout(labels):

    positive_count = labels.count(
        "positive"
    )

    neutral_count = labels.count(
        "neutral"
    )

    negative_count = labels.count(
        "negative"
    )

    latest_label = labels[-1]

    negative_streak = (
        calculate_negative_streak(
            labels
        )
    )

    volatility = calculate_volatility(
        labels
    )

    recovery_score = calculate_recovery(
        labels
    )

    recent_trend = calculate_recent_trend(
        labels
    )

    if (
        negative_count >= 5
        and negative_streak >= 3
        and latest_label == "negative"
    ):

        return {
            "state": "Severe Burnout",
            "prompt_mode": "motivation"
        }

    if (
        negative_count >= 4
        and latest_label == "negative"
        and recovery_score == 0
    ):

        return {
            "state": "Burnout Risk",
            "prompt_mode": "motivation"
        }

    if (
        volatility >= 5
        and positive_count >= 2
        and negative_count >= 2
    ):

        return {
            "state": "Emotional Instability",
            "prompt_mode": "support"
        }

    if (
        neutral_count >= 3
        or (
            negative_count >= 3
            and recovery_score >= 1
        )
    ):

        return {
            "state": "Adjustment Needed",
            "prompt_mode": "adjustment"
        }

    if (
        positive_count >= 3
        and recent_trend > 0
    ):

        return {
            "state": "Healthy",
            "prompt_mode": "congrats"
        }

    return {
        "state": "Stable",
        "prompt_mode": "support"
    }