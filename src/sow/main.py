#!/usr/bin/env python
import warnings
from datetime import datetime
from sow.crew import Sow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the Scope of Work crew with mock input data.
    """
    inputs = {
        'Client': 'Alice from BrandCo  ',
        'Contractor': 'Bob from DevGuru',
        'raw_description': '''

        We are planning to develop a modern Shopify-based e-commerce site that supports responsive design, payment gateway integration, SEO, and product listing features. The project should be completed in 4 weeks, with a clear deliverables list and limited revision rounds.
        ''',
        'current_year': str(datetime.now().year)
    }


    try:
        Sow().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Sow().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Sow().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Sow().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
