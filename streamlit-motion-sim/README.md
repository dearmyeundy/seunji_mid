# Streamlit Motion Simulation

This project is a Streamlit web application designed to visualize and compare uniform motion and free fall motion. It provides real-time simulations of velocity-time ($v-t$) and position-time ($s-t$) graphs, allowing students to input various parameters and observe the effects on motion and the corresponding graphs.

## Project Structure

The project is organized as follows:

```
streamlit-motion-sim
├── app
│   ├── streamlit_app.py       # Main entry point for the Streamlit application
│   ├── simulations.py          # Physics calculations for uniform motion and free fall
│   ├── plot.py                 # Graph generation for $v-t$ and $s-t$ visualizations
│   ├── controls.py             # User interface elements for input controls
│   └── utils.py                # Utility functions for data validation and formatting
├── configs
│   └── default.yaml            # Configuration settings for default values
├── notebooks
│   └── exploration.ipynb       # Jupyter notebook for exploratory data analysis
├── tests
│   ├── test_simulations.py     # Unit tests for simulations.py
│   └── test_plot.py            # Unit tests for plot.py
├── .devcontainer
│   ├── devcontainer.json       # Development container configuration
│   └── Dockerfile              # Instructions for building the Docker image
├── .gitignore                  # Files and directories to ignore by Git
├── requirements.txt            # List of required Python packages
└── README.md                   # Documentation for the project
```

## Features

- **Real-time Simulation**: Users can input initial velocity, acceleration, and time intervals to simulate uniform motion and free fall.
- **Interactive Graphs**: The application generates $v-t$ and $s-t$ graphs that update in real-time based on user inputs.
- **User-Friendly Interface**: Input controls are designed to be intuitive, allowing easy adjustments to simulation parameters.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-motion-sim
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run app/streamlit_app.py
   ```

## Usage

- Open the application in your web browser.
- Use the input controls to set the initial conditions for the simulation.
- Observe the changes in the $v-t$ and $s-t$ graphs as you adjust the parameters.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.