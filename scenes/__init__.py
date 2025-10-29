"""
Scenes package for CAS (Cultural Alien Sampler) video
"""
from .general_problem import GeneralProblem
from .creative_paradox import CreativeParadox
from .concept_reframing import ConceptReframing
from .llm_problem import LLMProblem
from .open_ended_agent import OpenEndedAgent
from .introducing_cas_solution import IntroducingCASSolution

__all__ = [
    'GeneralProblem',
    'CreativeParadox',
    'ConceptReframing',
    'LLMProblem',
    'OpenEndedAgent',
    'IntroducingCASSolution',
    'EvolutionaryTree',
    'CAMShowcase'
]