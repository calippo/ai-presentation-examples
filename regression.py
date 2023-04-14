import matplotlib.pyplot as plt
import numpy as np

# Generate random dataset
years = np.arange(2000, 2022)
prices = 100 + 0.5 * (years - 1999) + np.random.normal(0, 1, len(years))

# Calculate the best-fit line
slope, intercept = np.polyfit(years, prices, 1)
fit_line = slope * years + intercept

# Create figure with XKCD style
with plt.xkcd():
    fig, ax = plt.subplots()

    # Plot data points
    ax.plot(years, prices, 'o', label='Sneaker Prices')

    # Set x and y axis labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Price ($)')
    ax.set_title('Sneaker Prices over Time')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()

# Create figure with XKCD style
with plt.xkcd():
    fig, ax = plt.subplots()

    # Plot data points and best-fit line
    ax.plot(years, prices, 'o', label='Sneaker Prices')
    ax.plot(years, fit_line, label='Model')

    # Set x and y axis labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Price ($)')
    ax.set_title('Sneaker Prices over Time')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()

# Create figure with XKCD style
with plt.xkcd():
    fig, ax = plt.subplots()

    # Plot data points and best-fit line
    ax.plot(years, fit_line, label='Model')

    # Set x and y axis labels and title
    ax.set_xlabel('Year')
    ax.set_title('Sneaker Prices over Time')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()

    years_2030 = np.arange(2000, 2031)  # include 2030
    fit_line_2030 = slope * years_2030 + intercept

    fig, ax = plt.subplots()

    # Plot fitted line
    ax.plot(years_2030, fit_line_2030, label='Model')

    # Set x and y axis labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Price ($)')
    ax.set_title('Predict values from 2020 to 2030')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()
