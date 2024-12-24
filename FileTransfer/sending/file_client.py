import socket
import os
import zipfile

def compress_folder(folder_path):
    zip_path = folder_path + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, rel_path)
    return zip_path

def send_file(file_path, server_host, server_port):
    zip_file = compress_folder(file_path)
    print(f"Compressed file: {zip_file}")

    file_size = os.path.getsize(zip_file)

    # connect
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # send name, size and file
    metadata = f"{os.path.basename(zip_file)}|{file_size}"
    client_socket.sendall(metadata.encode())

    with open(zip_file, "rb") as file:
        bytes_sent = 0
        while bytes_sent < file_size:
            data = file.read(4096)
            client_socket.sendall(data)
            bytes_sent += len(data)
            print(f"Sent {bytes_sent}/{file_size} bytes")

    print("File sent succesfully")
    client_socket.close()

if __name__ == "__main__":
    folder_to_send = "/send"
    server_ip = "file_server"
    server_port = 5000
    
    send_file(folder_to_send, server_ip, server_port)