# IntelliAgentTeam: AI-Powered Project Planning System

This project is a system that uses artificial intelligence technologies to help create comprehensive project plans, utilizing a multi-expert approach.

## Features

- **Multi-Expert Approach**: Provides comprehensive analysis using AI agents in different roles (Project Manager, UX Designer, Software Architect, Team Leader).
- **Expert Interaction**: Simulates a real discussion environment with sequential information flow between expert AI agents.
- **Comprehensive Analysis**: Each expert conducts detailed analyses in their field, addressing different aspects of the project.
- **Terminal Output**: All expert opinions and analyses are presented clearly in the console.
- **Modular Architecture**: Easily extensible structure that allows new features to be added.

## Requirements

- Python 3.8 or higher
- Gemini API key (Google AI Studio)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Yaman-yagiz/IntelliAgentTeam.git
   cd IntelliAgentTeam
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Gemini API key:
   ```
   # Add your API key to the .env file
   GEMINI_API_KEY=your_api_key
   ```

## Usage

1. Add your project description to the `src/data/project_description.txt` file.

2. Run the program:
   ```
   python main.py
   ```

3. Analysis results will be displayed in the terminal.

## Project Structure

```
├── main.py                      # Main program
├── requirements.txt             # Dependencies
├── .env                         # Environmental variables
├── src/                         # Source code
│   ├── agents/                  # Agent modules
│   │   ├── __init__.py          
│   │   └── agents.py            
│   ├── core/                    # Core moduls
│   │   ├── __init__.py          
│   │   └── config.py            
│   ├── data/                    # Data and content
│   │   ├── __init__.py          
│   │   ├── project_description.txt  # Project description
│   │   └── instructions/        # Agent instructions
│   └── utils/                   # Helper modules
│       ├── __init__.py          
│       └── helpers.py           
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.