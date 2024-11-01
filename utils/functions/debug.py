import streamlit as st
import os


# 디버깅용 지우는 함수
class Debug:
    @staticmethod
    def my_openai_api_key():
        st.session_state["openai_api_key"] = os.environ["OPENAI_API_KEY_PROJECT"]
        st.session_state["openai_api_key_check"] = True

    @staticmethod
    def my_anthropic_api_key():
        st.session_state["claude_api_key"] = os.environ["ANTHROPIC_API_KEY"]
        st.session_state["claude_api_key_check"] = True
