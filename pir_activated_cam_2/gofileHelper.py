import requests
import logging
import os
import my_secrets

GETSERVER_URL = "https://api.gofile.io/getServer"
UPLOAD_URL = "https://{}.gofile.io/uploadFile"


class gofileHelper:
    def __init__(self):
        self.server = self.get_server()
        self.token = my_secrets.gofile_token
        self.gofile_folder = my_secrets.gofile_folder

    def get_server(self) -> str:
        """
        Get the best possible gofile server as determined by the gofile API.

        Parameters
        ----------
        None

        Returns
        -------
        server : str
            The best available server on gofile to receive files
        """
        resp = requests.get(GETSERVER_URL)
        server = None
        if resp.json()["status"] == "ok":
            server = resp.json()["data"]["server"]
        logging.info(f"Gofile server: {server}")
        return server

    def upload_file(self, path) -> dict:
        """
        Upload a file with the gofile API.

        Parameters
        ----------
        path : str
            path to the file you want to upload

        Returns
        -------
        resp_json : dict
            The json response after uploading a file.
        """
        assert self.server, "self.server cannot be None"

        # prepare post api request
        url = UPLOAD_URL.format(self.server)
        parms = {"token": self.token, "folderId": self.gofile_folder}
        resp_json = None

        # open specified file, submit post request, collect json response
        with open(path, "rb") as file:
            resp = requests.post(url, files={os.path.basename(path): file}, data=parms)
            logging.info(f"Gofile Response: {resp.json()}")
            resp_json = resp.json()

        return resp_json
