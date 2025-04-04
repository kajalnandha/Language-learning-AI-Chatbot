# Language Learning AI Chatbot

## Project Overview
The **Language Learning AI Chatbot** is an interactive conversational agent designed to assist users in learning a new language. It leverages OpenAI models and LangChain to provide real-time feedback, assess user proficiency, and offer tailored language-learning experiences.

## Features
- **Proficiency Assessment**: Detects the user’s known language and proficiency level.
- **Conversation Scenes**: Generates context-based conversation scenarios.
- **Mistake Tracking & Instant Feedback**: Identifies user mistakes and provides real-time corrections.
- **Mistake History Storage**: Stores only mistake history in an SQLite database for analysis.
- **Fixed Difficulty Levels**: Beginner, Intermediate, and Advanced.
- **Mistake Categorization**: Classifies errors into Grammar, Vocabulary, and Sentence Structure.
- **Synonyms & Alternative Words**: Provides alternative words for vocabulary mistakes.
- **Final Summary Report**: Generates a session-end report summarizing mistakes and areas for improvement.

## Tech Stack
- **Programming Language**: Python
- **Machine Learning Models**: OpenAI GPT-based models
- **Frameworks & Libraries**: LangChain, SQLite, Pandas, Numpy
- **Data Storage**: SQLite database for mistake tracking
- **Visualization**: Matplotlib, Seaborn (for potential analytics)

## System Architecture
1. **User Input** → User interacts with the chatbot in the target language.
2. **Language Detection & Proficiency Assessment** → Identifies the user's proficiency level.
3. **Conversation Scene Generation** → Sets a relevant conversation topic.
4. **Mistake Detection & Correction** → Provides real-time feedback and categorizes errors.
5. **Mistake Storage** → Stores mistakes in SQLite for session summary.
6. **Session Summary** → Generates an overview of user mistakes and learning suggestions.

## Installation Guide
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/language-learning-chatbot.git
   cd language-learning-chatbot
   ```
2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Chatbot**:
   ```bash
   python chatbot.py
   ```

## Usage
1. Run the chatbot script.
2. Select your known language and proficiency level.
3. Engage in a conversation and receive real-time corrections.
4. Review the final session summary at the end.

## Deliverables
- Python script (chatbot.py)
- Documentation & system architecture diagram
- SQLite database (mistake history)
- Recorded demo video

## Future Enhancements
- **Progress Tracking Over Sessions**
- **Speech Recognition & Text-to-Speech Integration**
- **Multilingual Support**
- **Gamification & Reward System**

## Contributors
- **Kajal Nandha** (Project Lead & Developer)

## License
This project is licensed under the MIT License.

