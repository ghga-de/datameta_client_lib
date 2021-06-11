# datameta-client-lib
DataMeta

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import datameta_client_lib
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import datameta_client_lib
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import datameta_client_lib
from pprint import pprint
from datameta_client_lib.api import authentication_and_users_api
from datameta_client_lib.model.api_key_list import ApiKeyList
from datameta_client_lib.model.create_token_request import CreateTokenRequest
from datameta_client_lib.model.error_model import ErrorModel
from datameta_client_lib.model.password_change import PasswordChange
from datameta_client_lib.model.user_session import UserSession
from datameta_client_lib.model.user_update_request import UserUpdateRequest
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = datameta_client_lib.Configuration(
    host = "https://raw.githubusercontent.com/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = datameta_client_lib.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with datameta_client_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_and_users_api.AuthenticationAndUsersApi(api_client)
    create_token_request = CreateTokenRequest(
        email="email_example",
        password="password_example",
        label="label_example",
        expires="expires_example",
    ) # CreateTokenRequest | Credentials to use (optional when using cookie sessions), a label for the ApiKey to be created and the date it expires. (optional)

    try:
        # Create new API Key/Token
        api_response = api_instance.create_api_key(create_token_request=create_token_request)
        pprint(api_response)
    except datameta_client_lib.ApiException as e:
        print("Exception when calling AuthenticationAndUsersApi->create_api_key: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://raw.githubusercontent.com/api/v0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationAndUsersApi* | [**create_api_key**](docs/AuthenticationAndUsersApi.md#create_api_key) | **POST** /keys | Create new API Key/Token
*AuthenticationAndUsersApi* | [**delete_api_key**](docs/AuthenticationAndUsersApi.md#delete_api_key) | **DELETE** /keys/{id} | Delete ApiKey by label
*AuthenticationAndUsersApi* | [**get_user_api_keys**](docs/AuthenticationAndUsersApi.md#get_user_api_keys) | **GET** /users/{id}/keys | All API keys for a user
*AuthenticationAndUsersApi* | [**set_user_password**](docs/AuthenticationAndUsersApi.md#set_user_password) | **PUT** /users/{id}/password | Update a user&#39;s password
*AuthenticationAndUsersApi* | [**user_update_request**](docs/AuthenticationAndUsersApi.md#user_update_request) | **PUT** /users/{id} | Update a user&#39;s credentials and status
*FilesApi* | [**create_file**](docs/FilesApi.md#create_file) | **POST** /files | Create a New File
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /files/{id} | Delete Not-Submitted File
*FilesApi* | [**get_file**](docs/FilesApi.md#get_file) | **GET** /files/{id} | Get Details for A File
*FilesApi* | [**update_file**](docs/FilesApi.md#update_file) | **PUT** /files/{id} | Update File Details
*GroupsApi* | [**change_group_name**](docs/GroupsApi.md#change_group_name) | **PUT** /groups/{id} | Change the name of a group.
*GroupsApi* | [**get_group_submissions**](docs/GroupsApi.md#get_group_submissions) | **GET** /groups/{id}/submissions | Get A List of All Submissions of A Group.
*MetadataApi* | [**create_meta_data_set**](docs/MetadataApi.md#create_meta_data_set) | **POST** /metadatasets | Create a New MetaDataSet
*MetadataApi* | [**create_meta_datum**](docs/MetadataApi.md#create_meta_datum) | **POST** /metadata | Create a New MetaDatum
*MetadataApi* | [**delete_metadata_set**](docs/MetadataApi.md#delete_metadata_set) | **DELETE** /metadatasets/{id} | Delete Not-Submitted Metadataset
*MetadataApi* | [**get_meta_data**](docs/MetadataApi.md#get_meta_data) | **GET** /metadata | Get metadata definitions
*MetadataApi* | [**get_meta_data_set**](docs/MetadataApi.md#get_meta_data_set) | **GET** /metadatasets/{id} | Get Details for a MetaDataSet
*MetadataApi* | [**get_meta_data_sets**](docs/MetadataApi.md#get_meta_data_sets) | **GET** /metadatasets | Query metadatasets
*MetadataApi* | [**update_meta_datum**](docs/MetadataApi.md#update_meta_datum) | **PUT** /metadata/{id} | Update a MetaDatum
*RemoteProcedureCallsApi* | [**bulk_delete_staged_files**](docs/RemoteProcedureCallsApi.md#bulk_delete_staged_files) | **POST** /rpc/delete-files | Bulk-delete Staged Files
*RemoteProcedureCallsApi* | [**bulk_delete_staged_meta_data_sets**](docs/RemoteProcedureCallsApi.md#bulk_delete_staged_meta_data_sets) | **POST** /rpc/delete-metadatasets | Bulk-delete Staged MetaDataSets
*RemoteProcedureCallsApi* | [**get_file_url**](docs/RemoteProcedureCallsApi.md#get_file_url) | **GET** /rpc/get-file-url/{id} | [Not RESTful]: Redirects to a temporary, pre-signed HTTP-URL for downloading a file.
*RemoteProcedureCallsApi* | [**get_user_information**](docs/RemoteProcedureCallsApi.md#get_user_information) | **GET** /rpc/whoami | [Not RESTful]: Returns information about the authenticated user
*ServerApi* | [**get_server_info**](docs/ServerApi.md#get_server_info) | **GET** /server | Get DataMeta server information
*ServicesApi* | [**get_service_info**](docs/ServicesApi.md#get_service_info) | **GET** /services | Get Services information
*ServicesApi* | [**post_service**](docs/ServicesApi.md#post_service) | **POST** /services | Create a new service.
*ServicesApi* | [**put_service**](docs/ServicesApi.md#put_service) | **PUT** /services/{id} | Update a specific service.
*ServicesApi* | [**service_set_meta_datum**](docs/ServicesApi.md#service_set_meta_datum) | **POST** /service-execution/{serviceId}/{metadatasetId} | Endpoint to store the result of a service execution for a single metadataset
*SettingsApi* | [**app_settings**](docs/SettingsApi.md#app_settings) | **GET** /appsettings | GET all AppSettings
*SettingsApi* | [**update_app_settings**](docs/SettingsApi.md#update_app_settings) | **PUT** /appsettings/{id} | Update a specific appsetting. This is an administrative Endpoint that is not accessible for regular users.
*SubmissionsApi* | [**create_submission**](docs/SubmissionsApi.md#create_submission) | **POST** /submissions | Create a New Submission
*SubmissionsApi* | [**get_group_submissions**](docs/SubmissionsApi.md#get_group_submissions) | **GET** /groups/{id}/submissions | Get A List of All Submissions of A Group.
*SubmissionsApi* | [**prevalidate_submission**](docs/SubmissionsApi.md#prevalidate_submission) | **POST** /presubvalidation | Pre-validate a submission
*UserApi* | [**get_registration_settings**](docs/UserApi.md#get_registration_settings) | **GET** /registrationsettings | Get details for the registration view
*UserApi* | [**post_registration**](docs/UserApi.md#post_registration) | **POST** /registrations | Create a new user registration request


## Documentation For Models

 - [ApiKeyList](docs/ApiKeyList.md)
 - [AppSettingsResponse](docs/AppSettingsResponse.md)
 - [AppSettingsUpdateRequest](docs/AppSettingsUpdateRequest.md)
 - [CreateTokenRequest](docs/CreateTokenRequest.md)
 - [Error](docs/Error.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [FileAnnouncement](docs/FileAnnouncement.md)
 - [FileResponse](docs/FileResponse.md)
 - [FileUpdateRequest](docs/FileUpdateRequest.md)
 - [FileUploadResponse](docs/FileUploadResponse.md)
 - [FileUrl](docs/FileUrl.md)
 - [GroupSubmissions](docs/GroupSubmissions.md)
 - [GroupUpdateRequest](docs/GroupUpdateRequest.md)
 - [Identifier](docs/Identifier.md)
 - [MetaDataResponse](docs/MetaDataResponse.md)
 - [MetaDataSet](docs/MetaDataSet.md)
 - [MetaDataSetResponse](docs/MetaDataSetResponse.md)
 - [MetaDataSetServiceExecution](docs/MetaDataSetServiceExecution.md)
 - [MetaDatum](docs/MetaDatum.md)
 - [MetaDatumResponse](docs/MetaDatumResponse.md)
 - [NullableIdentifier](docs/NullableIdentifier.md)
 - [PasswordChange](docs/PasswordChange.md)
 - [RegisterSettingsResponse](docs/RegisterSettingsResponse.md)
 - [RegistrationRequest](docs/RegistrationRequest.md)
 - [ServerInfoResponse](docs/ServerInfoResponse.md)
 - [ServiceExecution](docs/ServiceExecution.md)
 - [ServiceRequest](docs/ServiceRequest.md)
 - [ServiceResponse](docs/ServiceResponse.md)
 - [ServiceUpdateRequest](docs/ServiceUpdateRequest.md)
 - [Services](docs/Services.md)
 - [StagedFiles](docs/StagedFiles.md)
 - [StagedMetaDataSets](docs/StagedMetaDataSets.md)
 - [SubmissionRequest](docs/SubmissionRequest.md)
 - [SubmissionResponse](docs/SubmissionResponse.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserResponseGroup](docs/UserResponseGroup.md)
 - [UserSession](docs/UserSession.md)
 - [UserUpdateRequest](docs/UserUpdateRequest.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## cookieAuth

- **Type**: API key
- **API key parameter name**: datameta
- **Location**: 


## Author

leon.kuchenbecker@uni-tuebingen.de


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in datameta_client_lib.apis and datameta_client_lib.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from datameta_client_lib.api.default_api import DefaultApi`
- `from datameta_client_lib.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import datameta_client_lib
from datameta_client_lib.apis import *
from datameta_client_lib.models import *
```

