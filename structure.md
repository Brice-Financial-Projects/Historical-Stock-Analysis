# Historical Stock Analysis File Structure

historical-stock-analysis/
├── data/                        # Folder for storing downloaded data (optional)
├── notebooks/                   # Folder for Jupyter notebooks (for EDA or experiments)
├── src/                         # Folder for Python source files
│   ├── data_retrieval.py        # Script to handle API calls and data retrieval
│   ├── analysis.py              # Script for analysis functions (e.g., returns, moving averages)
│   └── visualization.py         # Script for plotting and visualization
├── README.md                    # Project overview and setup instructions
├── environmennt.yml             # List of dependencies
└── main.py                      # Main script to run the analysis and visualizations

## Explanation of Each Folder and File

**data/**: Optional, used to save downloaded stock data as CSV files for offline analysis.
**notebooks/**: For Jupyter notebooks where you can experiment with code, perform exploratory data analysis (EDA), or test functions before moving them to src.
**src/**: Contains modular Python files to handle specific tasks, such as data retrieval, analysis, and visualization.
**data_retrieval.py**: Manages API requests to Tiingo and organizes data retrieval functions.
**analysis.py**: Contains analysis functions like calculating returns and moving averages.
**visualization.py**: Handles visualizations using libraries like Matplotlib.
**README.md**: Provides an overview, project objectives, and setup instructions.
**requirements.txt**: Lists required libraries (e.g., requests, pandas, matplotlib) for easy installation.
**main.py**: Main script to run the project, tying together data retrieval, analysis, and visualization.
