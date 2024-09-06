# Fleur Roms API
The Fleur ROM API is a Flask-based API that provides a streamlined and platform-specific solution for retrieving all available custom ROMs for the device ```Fleur (Poco M4 Pro 4G)```. This API offers a centralized resource for developers and enthusiasts to access and manage custom ROM data, ensuring easy integration and up-to-date information on ROM availability for this specific device.

This API is available at [API](https://fleur-roms-api.onrender.com/roms) and can be accessed by exploring the various API endpoints detailed further in the documentation.

## Note
It might delay for your first request , but once you get ```Server Up and Running at '/' endpoint``` , you are good to go.

## Local Checkout of Code
To set up the project locally, follow these steps:
### 1. Fork and Clone the Repo:
Fork the repository to your GitHub account and clone it to your local machine:
```
git clone https://github.com/your-username/fleur-roms-api.git
```
### 2. Create a Virtual Environment:
Set up a Python virtual environment:
```
python -m venv venv
```
Install Requirements.txt
```
pip install -r requirements.txt
```
### 3.Activate the Virtual Environment:
- On Windows:
  ```
   venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```
### 4.Set Up Environment Variables and Run the Server:
Configure your environment variables `(.env)` as per `.sample.env`, then start the server with Gunicorn:
```
gunicorn -c gunicorn.conf.py app:app
```

## API endpoints
 ### for recovery options
 #### 1. List all recovery options ```GET Request```
        /recovery
 #### 2. Add new recovery  record ```POST Request```
        /recovery

```
Request Parameters (json body)
- name (string, required):
The name of the recovery record.

- version (string, required):
The version of the recovery record.

- modified (string, required):
The date and time when the recovery record was last modified. This should be in ISO format (e.g., 2024-08-19).

- tested (boolean, required):
Indicates whether the recovery has been tested (true or false).

- download (string, required):
A URL pointing to the location where the recovery file can be downloaded.
```

### for Roms actions
#### 1. List all available Rom options ```GET Request```
     /roms
#### 2. Search for a rom ``` GET Request ``` (eg. Lineage OS)
     /rom/name
     (eg. /rom/Lineage OS)
#### 3. Add new Rom  record ```POST Request```
        /rom
        
```       
Request Parameters(json body)

- name (string, required):
The name of the ROM. This will be stored in lowercase.

- description (string, optional):
A brief description of the ROM.

- tested (boolean, optional):
Indicates whether the ROM has been tested (true or false).

- android_version (string, optional):
The Android version associated with the ROM.

- build (object, required):
An object representing the build details.

- build.tested (boolean, required):
Indicates whether the build has been tested (true or false).

- build.download (string, required):
A URL pointing to the location where the build can be downloaded.

- build.modified (string, required):
The date and time when the build was last modified. This should be in ISO 8601 format (e.g., 2024-08-19).
```
#### 4. Add new build record for existing rom ``` POST Request ```
     /build
```
Request Parameters (json body)
- rom_id (string, required):
The unique ID of the ROM to which the new build will be added.

- modified (string, required):
The date and time when the build was last modified. This should be in ISO 8601 format (e.g., 2024-08-19T12:34:56).

- tested (boolean, required):
Indicates whether the build has been tested (true or false).

- download (string, required):
A URL pointing to the location where the build file can be downloaded.
```
### For Getting Steps:
  #### Steps ```GET Request```
     /steps
  
## Thanks For Using:
Have Poco M4 Pro 4g , enjoy the api. 
My Personal Choice is Lineage OS...
