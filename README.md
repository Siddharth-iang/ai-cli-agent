# AI CLI Agent
A powerful AI-powered command-line interface that combines file system operations with intelligent AI assistance.

## 🚀 Features
### Core Capabilities
- **🧠 AI Integration**: Powered by Google Gemini 2.5 Flash for intelligent responses
- **📁 File Operations**: Complete file system management with security controls
- **🐍 Python Execution**: Run Python scripts with argument passing
- **📊 Calculator**: Built-in mathematical expression evaluator
- **🔧 Function Calling**: AI can automatically execute file operations

### Available Functions
- `get_files_info()` - List directory contents with metadata
- `get_file_content()` - Read file contents with character limits
- `write_file()` - Create/update files with directory creation
- `run_python_file()` - Execute Python files with arguments

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- UV package manager
- Google Gemini API key

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Siddharth-iang/ai-cli-agent.git
   cd ai-cli-agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure API key**
   ```bash
   # Create .env file with your Gemini API key
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

## 📖 Usage

### Basic AI Chat
```bash
uv run main.py "your question here"
```

### With Verbose Output
```bash
uv run main.py "your question" --verbose
```

### Function Calling Examples
```bash
# List files in current directory
uv run main.py "what files are in root directory"

# List files in specific directory
uv run main.py "show me files in calculator folder"

# Run calculator
uv run main.py "calculate 3 + 5 * 2"
```

### File Operations
```bash
# Read file content
uv run main.py "read the contents of config.py"

# Write to file
uv run main.py "create a new file called test.txt with hello world content"
```

## 🏗️ Project Structure

```
ai-cli-agent/
├── 📁 calculator/           # Mathematical expression evaluator
│   ├── main.py            # Calculator CLI interface
│   ├── pkg/
│   │   ├── calculator.py    # Core calculator logic
│   │   └── render.py       # JSON output formatter
│   └── tests.py           # Unit tests
├── 📁 functions/            # File system operations
│   ├── get_files_info.py   # Directory listing
│   ├── get_files_content.py # File reading
│   ├── write_files.py      # File writing
│   └── run_python_file.py  # Python execution
├── 📄 main.py              # Main AI CLI interface
├── 📄 config.py            # Configuration settings
├── 📄 pyproject.toml       # Project dependencies
└── 📄 .env                 # API keys (not tracked)
```

## 🧪 Testing

### Run Calculator Tests
```bash
uv run calculator/tests.py
```

### Run File Operation Tests
```bash
uv run tests.py
```

## 🔒 Security Features

- **Path Validation**: All file operations restricted to working directory
- **Directory Traversal Prevention**: Cannot access parent directories
- **API Key Protection**: Environment variables only, no hardcoded keys

## 🎯 Use Cases

### Developers
- Quick file system operations without leaving editor
- Automated script execution with AI assistance
- Mathematical calculations via natural language
- Code review and analysis

### System Administrators
- Secure file management with audit trails
- Automated deployment scripts
- Configuration management

### Data Scientists
- Quick data file analysis
- Experiment result tracking
- Automated report generation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly: `uv run tests.py`
5. Commit: `git add . && git commit -m "description"`
6. Push: `git push origin feature-name`
7. Create Pull Request

## 📄 License
This project is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments
- **Google Gemini** - For providing the powerful AI model
- **UV** - For modern Python package management
- **Python Community** - For the robust ecosystem

---

**Built with ❤️ by [Siddharth-iang](https://github.com/Siddharth-iang)**

