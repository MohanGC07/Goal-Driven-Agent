import os
from groq import Groq


class GoalAgent:
    def __init__(self, max_steps=5):
        self.max_steps = max_steps
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # -----------------------
    # Generic LLM Caller
    # -----------------------
    def call_llm(self, messages, temperature=0.3, max_tokens=600):
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()

    # -----------------------
    # 1️⃣ PLAN
    # -----------------------
    def plan(self, goal):
        messages = [
            {
                "role": "system",
                "content": "You are a strategic planner. Break the goal into clear numbered steps."
            },
            {
                "role": "user",
                "content": f"Create a step-by-step plan for this goal:\n{goal}"
            }
        ]
        return self.call_llm(messages)

    # -----------------------
    # 2️⃣ EXECUTE STEP
    # -----------------------
    def execute_step(self, step):
        messages = [
            {
                "role": "system",
                "content": "You are an executor. Perform the step clearly and practically."
            },
            {
                "role": "user",
                "content": f"Execute this step:\n{step}"
            }
        ]
        return self.call_llm(messages)

    # -----------------------
    # 3️⃣ REFLECT
    # -----------------------
    def reflect(self, goal, step, result):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a critic. Decide if the goal is achieved. "
                    "Respond ONLY with CONTINUE or STOP and a short reason."
                )
            },
            {
                "role": "user",
                "content": f"""
Goal: {goal}

Step: {step}

Result: {result}

Should we continue?
"""
            }
        ]
        return self.call_llm(messages)

    # -----------------------
    # 4️⃣ FINAL SYNTHESIS
    # -----------------------
    def synthesize_final(self, goal, execution_history):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a final report generator. "
                    "Based on all steps executed, produce a clear final answer "
                    "that directly fulfills the original goal."
                )
            },
            {
                "role": "user",
                "content": f"""
Original Goal:
{goal}

Execution History:
{execution_history}

Provide the final consolidated answer.
"""
            }
        ]
        return self.call_llm(messages)

    # -----------------------
    # MAIN LOOP
    # -----------------------
    def run(self, goal):

        logs = []
        execution_history = ""

        # PLAN
        plan_text = self.plan(goal)
        logs.append(("PLAN", plan_text))

        steps = [s for s in plan_text.split("\n") if s.strip()]

        for i, step in enumerate(steps[:self.max_steps]):

            # EXECUTE
            result = self.execute_step(step)
            logs.append((f"EXECUTE STEP {i+1}", result))

            execution_history += f"\nStep {i+1}: {step}\nResult: {result}\n"

            # REFLECT
            reflection = self.reflect(goal, step, result)
            logs.append((f"REFLECTION {i+1}", reflection))

            if "STOP" in reflection.upper():
                logs.append(("STATUS", "Agent decided to stop early."))
                break

        # FINAL SYNTHESIS
        final_answer = self.synthesize_final(goal, execution_history)
        logs.append(("FINAL ANSWER", final_answer))

        return logs
