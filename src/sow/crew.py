from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Sow:
    """Scope of Work Generator Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def InputParser_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['InputParser_Agent'],
            verbose=True)

    @agent
    def ScopeBuilder_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ScopeBuilder_Agent'],
            verbose=True)

    @agent
    def ContentWriter_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ContentWriter_Agent'],
            verbose=True)

    @agent
    def PolicyAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['PolicyAgent'],
            verbose=True)

    @agent
    def QualityCheck_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['QualityCheck_Agent'],
            verbose=True)

    @agent
    def Formatter_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Formatter_Agent'],
            verbose=True)

    @task
    def parse_input_task(self) -> Task:
        return Task(config=self.tasks_config['parse_input_task'])

    @task
    def build_scope_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['build_scope_outline_task'],
            context=[self.parse_input_task()])

    @task
    def generate_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_content_task'],
            context=[self.parse_input_task(),self.build_scope_outline_task()])

    @task
    def insert_policy_clauses_task(self) -> Task:
        return Task(
            config=self.tasks_config['insert_policy_clauses_task'],
            context=[self.generate_content_task()])

    @task
    def quality_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_review_task'],
            context=[self.insert_policy_clauses_task()])

    @task
    def format_sow_document_task(self) -> Task:
        return Task(
            config=self.tasks_config['format_sow_document_task'], 
            context=[self.quality_review_task()],
            output_file='scope_of_work.md')

    @crew
    def crew(self) -> Crew:
        """Creates the Scope of Work Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
