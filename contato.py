import streamlit as st

def contact():
    st.header("Entre em contato conosco")

    contact_form = """
        <form action="https://formsubmit.co/kaique.miranda1910@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Seu nome" required>
            <input type="email" name="email" placeholder="Seu email" required>
            <textarea name="message" placeholder="Digite sua mensagem aqui"></textarea>
            <button type="submit">Enviar</button>
        </form>
        """


    st.markdown(contact_form, unsafe_allow_html=True)


    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")
