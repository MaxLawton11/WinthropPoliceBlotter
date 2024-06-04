import matplotlib.pyplot as plt
import numpy as np

def value_to_color(value):
    """Returns an RGB color value transitioning from green (0) to yellow (0.5) to red (1) based on input value (0 to 1)."""
    if not 0 <= value <= 1:
        raise ValueError("Value must be between 0 and 1")
    if value <= 0.5:
        # Transition from green to yellow
        red = 2 * value
        green = 1-red
        blue = 0
    else:
        # Transition from yellow to red
        red = 1
        green = 2 * (1 - value)
        blue = 0
    return (red, green, blue)

# Generate values and corresponding colors
values = np.linspace(0, 1, 100)
colors = [value_to_color(v) for v in values]

plt.figure(figsize=(10, 2))
plt.imshow([colors], aspect='auto')
plt.gca().axes.get_yaxis().set_visible(False)
plt.title('Color Transition from Green to Yellow to Red')
plt.xlabel('Value')
plt.show()
