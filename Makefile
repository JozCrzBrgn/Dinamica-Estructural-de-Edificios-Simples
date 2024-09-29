run:
# Corremos la app
	streamlit run streamlit_app.py

#? make install LIB="pytest"
install:
	pip install $(LIB) && pip freeze | findstr $(LIB) >> requirements.txt