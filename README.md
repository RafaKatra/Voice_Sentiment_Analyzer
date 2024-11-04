**Voice Sentiment Analyzer**
A sophisticated speech analysis system that performs real-time sentiment analysis by processing both speech content and voice characteristics. The system combines textual sentiment analysis with voice tone analysis to provide comprehensive emotional insights.
Description
The system captures audio input and analyzes it on multiple levels:

**Speech-to-text conversion (Greek language)**
Text translation to English
Sentiment analysis of text content
Voice characteristics analysis (intensity, speed, pitch)
Combined sentiment evaluation

Technical Features

**Real-time audio recording**
Greek speech recognition
Text translation (Greek to English)
Sentiment analysis using TextBlob
Voice tone analysis using librosa
Colored console output

**Prerequisites**

Python 3.6+
Microphone
Internet connection (for speech recognition and translation)
System audio capabilities

**How It Works**

Audio Recording:

Records audio for 15 seconds
10-second preparation countdown
Uses system's default microphone


Speech Processing:

Converts speech to text using Google's Speech Recognition
Translates Greek text to English
Performs sentiment analysis on translated text


Voice Analysis:

Analyzes voice intensity
Measures speech speed
Evaluates pitch characteristics


Combined Analysis:

Integrates text sentiment with voice characteristics
Provides weighted analysis results
Outputs comprehensive emotional assessment

Output Information
The system provides:

Transcribed text (Greek)
Text-based sentiment analysis
Voice characteristics:

Intensity (High/Low)
Speed (Fast/Slow)
Pitch (High/Low)

Combined sentiment conclusion

**Technical Details**

Speech Recognition: Uses Google's Speech Recognition API
Translation: Google Translate API
Sentiment Analysis: TextBlob library
Voice Analysis: librosa audio processing library
Console Interface: colorama for colored output

**Notes**

Ensure a quiet environment for better speech recognition
Speak clearly and at a normal pace
Internet connection required for speech recognition and translation
Results are for demonstration purposes only

Troubleshooting

**If speech isn't recognized:**

Check microphone settings
Ensure quiet surroundings
Verify internet connection


**If translation fails:**

Check internet connection
Try speaking more clearly
Ensure proper Greek pronunciation



**Limitations**

Requires stable internet connection
Best results in quiet environments
Speech recognition accuracy may vary
Translation quality affects sentiment analysis
Limited to 15-second recordings


