"""
Unit tests for Emotion Detection application.
"""
import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for emotion_detector function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup realistic Watson NLP responses for sample statements.
        """
        cls.mock_data = {
            "I am glad this happened": {
                'anger': 0.002, 'disgust': 0.001, 'fear': 0.001,
                'joy': 0.985, 'sadness': 0.005
            },
            "I am really mad about this": {
                'anger': 0.954, 'disgust': 0.021, 'fear': 0.008,
                'joy': 0.003, 'sadness': 0.014
            },
            "I feel disgusted just hearing about this": {
                'anger': 0.012, 'disgust': 0.945, 'fear': 0.011,
                'joy': 0.002, 'sadness': 0.030
            },
            "I am so sad about this": {
                'anger': 0.015, 'disgust': 0.005, 'fear': 0.012,
                'joy': 0.004, 'sadness': 0.964
            },
            "I am really afraid that this will happen": {
                'anger': 0.008, 'disgust': 0.004, 'fear': 0.971,
                'joy': 0.003, 'sadness': 0.014
            }
        }

    def _mock_post(self, url, json=None, headers=None, timeout=None):
        """
        Helper mock function returning genuine Watson NLP API payload structure.
        """
        text = json.get('raw_document', {}).get('text', '') if json else ''
        mock_response = Mock()

        if not text:
            mock_response.status_code = 400
            mock_response.json.return_value = {}
            return mock_response

        if text in self.mock_data:
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'emotionPredictions': [{
                    'emotion': self.mock_data[text]
                }]
            }
            return mock_response

        # Default fallback
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{
                'emotion': {
                    'anger': 0.1, 'disgust': 0.1, 'fear': 0.1,
                    'joy': 0.5, 'sadness': 0.2
                }
            }]
        }
        return mock_response

    @patch('requests.post')
    def test_emotion_detector_joy(self, mock_post):
        """Test dominant emotion joy for 'I am glad this happened'"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('requests.post')
    def test_emotion_detector_anger(self, mock_post):
        """Test dominant emotion anger for 'I am really mad about this'"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('requests.post')
    def test_emotion_detector_disgust(self, mock_post):
        """Test dominant emotion disgust for 'I feel disgusted just hearing about this'"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        """Test dominant emotion sadness for 'I am so sad about this'"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('requests.post')
    def test_emotion_detector_fear(self, mock_post):
        """Test dominant emotion fear for 'I am really afraid that this will happen'"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    @patch('requests.post')
    def test_output_keys_and_types(self, mock_post):
        """Test dictionary keys and return types"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("I am glad this happened")
        expected_keys = {'anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'}
        self.assertIsInstance(result, dict)
        self.assertEqual(set(result.keys()), expected_keys)
        self.assertIsInstance(result['dominant_emotion'], str)
        self.assertIsInstance(result['joy'], float)

    @patch('requests.post')
    def test_status_code_400_handling(self, mock_post):
        """Test error handling when API returns status code 400"""
        mock_resp = Mock()
        mock_resp.status_code = 400
        mock_post.return_value = mock_resp

        result = emotion_detector("")
        expected = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        self.assertEqual(result, expected)

    @patch('requests.post')
    def test_empty_input_handling(self, mock_post):
        """Test handling of empty string input"""
        mock_post.side_effect = self._mock_post
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
