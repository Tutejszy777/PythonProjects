# Transfer any files from one computer to another on local network

place files to be sent into the (send) folder  if you are awaiting for files they will be in folder (received_files)

to run server - docker compose up -d --build  on server
to check if it runs -  docker compose logs file_server 

to run sender - docker compose up -d --build
to send folder - docker compose run file_client (UPDATE IP BEFORE) 

