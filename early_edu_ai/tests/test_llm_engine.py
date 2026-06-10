import unittest
from unittest.mock import patch

from core.llm_engine import LLMEngine


class LLMEngineTests(unittest.TestCase):
    def test_generate_response_falls_back_without_hallucination(self):
        engine = LLMEngine()

        with patch('core.llm_engine.ollama.chat', side_effect=RuntimeError('Ollama unavailable')):
            answer = engine.generate_response(
                context='No relevant documents found.',
                query='What is the homework?',
                role='parent'
            )

        self.assertIsInstance(answer, str)
        self.assertIn('I do not have enough information', answer)


if __name__ == '__main__':
    unittest.main()
