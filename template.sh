# Creating directory
mkdir -p app/models
mkdir -p app/services
mkdir -p app/static
mkdir -p app/template
mkdir -p data

# Creating files
touch app/__init__.py
touch app/config.py
touch app/main.py
touch requirements.txt
touch app/models/__init__.py
touch app/models/vector_stor.py
touch app/services/__init__.py
touch app/services/llm_service.py
touch app/template/template.html

echo " Directory and files created successfully"