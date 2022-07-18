def getConfidenceIntervalByFeature(data, feature_x_name, feature_x_value, feature_y, bootstrap_repetition_factor,
                                        dataset_catagory):
    # Configure bootstrap
    transactions = data[data[feature_x_name] == feature_x_value][feature_y]

    sample_size = 10000
    bootstrap_size = int(bootstrap_repetition_factor * len(transactions))
    bootstrapped_means = np.empty(sample_size)
    for i in range(sample_size):
        bootstrapped_sample = transactions.sample(bootstrap_size, replace=True)
        x_bar = np.mean(bootstrapped_sample)  # Sample mean; Replace by median/percentile
        bootstrapped_means[i] = x_bar

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    # Mean & Standard deviation
    mean = np.mean(bootstrapped_means)
    standard_deviation = np.std(bootstrapped_means, ddof=1)  # ddof = 1 for un-biased estimates
    print("CI by " + feature_x_name + " == " + feature_x_value + " Mean ", mean, " S.D - ", standard_deviation)

    # Plot mean scores
    plt.figure()
    plt.hist(bootstrapped_means, bins=100)
    plt.grid()
    plt.show()

    # Compute Confidence Intervals

    # Strategy #1 - Bootstrap with CLT, which works on only mean
    # given that bootstrapped_means that follows Gaussian distribution: CLT
    confidence_interval_on_mean = [(mean - 1.96 * standard_deviation), (mean + 1.96 * standard_deviation)]
    print("C.I (on the mean)", confidence_interval_on_mean)

    # Strategy #2 - Pure Bootstrap , as CLT won't work for percentile
    confidence_interval_on_percentile = np.percentile(bootstrapped_means, [2.5, 97.5])
    print("C.I (on the percentile) by", confidence_interval_on_percentile)

    CI_length = confidence_interval_on_mean[1] - confidence_interval_on_mean[0]
    print("C.I length ", CI_length)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")