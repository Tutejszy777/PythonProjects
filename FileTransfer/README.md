
in bash
## Without yml

# Build server image
docker build -t file_server ./file_server

# Build client image
docker build -t file_client ./file_client

# Run Server in a Container
Run the server container, mapping port 5000

docker run -d --name server -p 5000:5000 file_server


# Run Client in a Container
Place your file or folder to send in a directory, e.g., ./data, and run the client container with the directory mounted:
docker run --rm -v $(pwd)/data:/app/data file_client python file_client.py "/app/data/example_folder" 127.0.0.1 5000

///////////////////////////////

# with yml 

Build and Run Containers:

docker-compose up --build

This will:
Start the file_server on port 5000.
Mount file_client/data to the client container for sending files.
Transfer Files:

Place the folder or file to be sent in file_client/send/
The client will automatically send the file to the server.
Received files will be stored in ~/received_files/.

Stop Containers:

docker-compose down
