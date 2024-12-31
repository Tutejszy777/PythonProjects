# Transfer any files from one computer to another.

# place files to be sent into the (send) folder
# if you are awaiting for files they will be in folder (received_files) (zipped or unziped check python code serv)

# to run server
# docker compose up -d --build  on server
# docker compose logs file_server (check if runs)

# to run sender
# docker compose up -d --build
# docker compose run file_client (sends folder) (UPDATE IP BEFORE) 

# REMEMBER TO CLEAN DOCKER AFTER ALL (Program works anyway)
