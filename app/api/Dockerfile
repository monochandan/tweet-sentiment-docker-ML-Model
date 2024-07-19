# Use a more recent version of Python
FROM python:3.10-alpine

# Install necessary build tools and libraries
RUN apk add --no-cache build-base gcc gfortran musl-dev linux-headers libgfortran lapack-dev freetype-dev libpng-dev openblas-dev

## setup working directory

# Copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
#RUN pip install --upgrade pip && \
#   pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"

# Copy the rest of the application code
COPY  . .

# Expose port
EXPOSE 5000

# define environment veriable
# ENV NAME World

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

