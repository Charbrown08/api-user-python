### FastAPI User Administration REST API

This is a basic REST API application created with FastAPI to manage users and their addresses. The API provides endpoints for creating, retrieving, updating, and deleting users, as well as for retrieving users by country in their addresses.


### Creating a Virtual Environment in Python

Before running the application, it's recommended to create a virtual environment to ensure that the project dependencies are installed in an isolated environment, without affecting other Python applications on your system. A virtual environment is a directory that contains a self-contained Python installation, allowing libraries and tools specific to your project to be kept separate from other projects. This practice prevents conflicts and ensures a clean and controlled development environment.

#### How to Create a Virtual Environment?

To create a virtual environment in Python, use the following command in your terminal or command prompt:

```bash
python -m venv venv
```

This command utilizes the `venv` module in Python to create a virtual environment named `venv` in the current directory. You can change the name `venv` to any other name you prefer for your virtual environment.


This process ensures that your project's dependencies are installed and run in an isolated environment, helping to avoid issues related to library versions and ensuring a consistent development experience for all users.

1. **Activate the Virtual Environment**

   Before running the application, make sure to activate your virtual environment (venv). You can do so by running the following command in your terminal or command prompt:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

2. **Install Dependencies**

   Ensure you have Python and pip installed. Then, install the dependencies by running:

   ```
   pip install fastapi uvicorn sqlalchemy
   ```

3. **Database Setup**

   Ensure you have a configured database. This code assumes the use of SQLAlchemy with a predefined database structure. Make sure to configure the database credentials in `config/database.py`.

4. **Run the Application**

   Run the application using the following command:

   ```
   uvicorn main:app --reload
   ```

   This will start the FastAPI server, and the API will be accessible at `http://localhost:8000`.

### API Endpoints

- **`POST /users`**
  - Create a new user with an address.
  - Input parameters: name, lastname, age, email, password, and address.
  
- **`GET /users`**
  - Retrieve all users with their addresses.
  
- **`GET /users/{id}`**
  - Retrieve a user by their ID with their address.
  
- **`PUT /users/{id}`**
  - Update an existing user and their address.
  - Input parameters: name, lastname, age, email, password, and address.
  
- **`DELETE /users/{id}`**
  - Delete a user by their ID with their address.
  
- **`GET /users/country/{country}`**
  - Retrieve users by the name of their country in the address.

### Data Models

- **User (`UserModel`)**: 
  - ID (Automatically generated)
  - Name
  - Lastname
  - Age
  - Email
  - Password
  - Address (`AddressModel`)
  
- **Address (`AddressModel`)**: 
  - ID (Automatically generated)
  - Address Line 1
  - Address Line 2
  - City
  - State
  - ZIP
  - Country

### Important Notes

- Requests and responses are handled in JSON format.
- The application handles errors, including cases where the user is not found.
- Endpoints have been provided for all operations specified in the challenge.



### Running Tests with Pytest

#### Installing Dependencies

Before running tests, make sure to install the testing framework pytest. You can install it within your virtual environment using the following command:

```bash
pip install pytest
```

#### Running All Tests

To execute all tests within your project, use the following command in your terminal or command prompt while your virtual environment is active:

```bash
pytest
```

This command will automatically discover and run all test functions in files matching the pattern `test_*.py` or `*_test.py` in your project directory and its subdirectories. Pytest will provide detailed output indicating which tests passed and which failed.

Remember to write your test functions following the naming conventions recognized by pytest (i.e., starting with `test_`), and place them in files that match the specified patterns for automatic discovery.

---

