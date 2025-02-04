import streamlit as st


def show() -> None:
    with st.sidebar:
        st.markdown(f"""
            <a href="/" style="color:black;text-decoration: none;">
                <div style="display:table;margin-top:-18.5rem;margin-left:0%;">
                    <img src="/app/static/ducky_logo2.png" width="60"><span style="color:white;">Ducky</span>
                    <span style="font-size: 0.8em; color: grey">&nbsp;&nbsp;v0.1.0</span>
                    <br>
                    <span style="font-size: 0.8em; margin-bottom: 2rem;">Your AI-powered software developer assistant!</span>
                </div>
            </a>
            <br>
                """, unsafe_allow_html=True)

        reload_button = st.button("↪︎  Reload Page")
        if reload_button:
            st.session_state.clear()
            st.rerun()
