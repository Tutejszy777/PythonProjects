import socket
import os
import zipfile

SAVE_DIR = "received_files"

def decompress_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"File decompressed to {extract_to}")

def start_server(host='0.0.0.0', port=5000):
    os.makedirs(SAVE_DIR, exist_ok=True)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.settimeout(60)  # Set timeout to avoid hanging indefinitely
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"Connection with {addr}")

            metadata = conn.recv(1024).decode()
            if not metadata:
                print("No metadata received. Closing connection.")
                conn.close()
                continue

            filename, filesize = metadata.split('|')
            filesize = int(filesize)
            print(f"Receiving {filename} ({filesize} bytes)")

            received_size = 0
            file_path = os.path.join(SAVE_DIR, filename)
            with open(file_path, 'wb') as file:
                while received_size < filesize:
                    data = conn.recv(4096)
                    if not data:
                        break
                    file.write(data)
                    received_size += len(data)
                    print(f"Progress: {received_size}/{filesize} bytes")

            if file_path.endswith('.zip'):
                decompress_file(file_path, SAVE_DIR)

            print(f"File {filename} received successfully")
        except socket.timeout:
            print("Socket timeout occurred. No connections within the time frame.")
        except ValueError as e:
            print(f"Error receiving metadata: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    start_server()