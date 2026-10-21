# Night, Street, Lamp, Endpoint

HTTP server that responds to GET requests with a greeting and the requested path.

## Local run

Run `python app.py` and open `http://localhost:8000/poetry`.

Expected response:

    Hello from LMS! 👋
    Path: /poetry

## Docker

Build the image:

    docker build -t night-street-lamp-endpoint .

Run the container:

    docker run --rm -p 127.0.0.1:8091:8000 night-street-lamp-endpoint

Open `http://localhost:8091/poetry`.

The application uses port `8000` and the name `LMS` by default. Both can be configured using the `PORT` and `APP` environment variables.