from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_joy = emotion_detector("I am glad this happened")
        self.assertTrue(result_joy.startswith("The given text has the emotion 'joy'"))

        result_anger = emotion_detector("I am really mad about this")
        self.assertTrue(result_anger.startswith("The given text has the emotion 'anger'"))

        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertTrue(result_disgust.startswith("The given text has the emotion 'disgust'"))

        result_sadness = emotion_detector("I am so sad about this")
        self.assertTrue(result_sadness.startswith("The given text has the emotion 'sadness'"))

        result_fear = emotion_detector("I am really afraid that this will happen")
        self.assertTrue(result_fear.startswith("The given text has the emotion 'fear'"))

if __name__ == "__main__":
    unittest.main()
