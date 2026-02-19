import streamlit as st
from agent import GoalAgent

st.set_page_config(page_title="Autonomous Goal Agent")

st.title("Goal Driven Autonomous Agent")

goal = st.text_input("Enter Your Goal")
max_steps = st.slider("Max Steps", 1, 10, 5)

if st.button("Run Agent") and goal:

    agent = GoalAgent(max_steps=max_steps)

    with st.spinner("Agent running full loop..."):
        logs = agent.run(goal)

    for title, content in logs:
        st.subheader(title)
        st.write(content)
