# PyTest_API_Pet - Educational Project


Project for Automated API Testing of the Website http://34.141.58.52:8000/docs#/

User Scenario:

Steps:

- Perform a registration request POST/register with valid user data and then delete the created user with the request DELETE/users/{id}.
Precondition: A user is registered in the system with the login alesia@mail.ru and the password 1234.

- Perform a login request POST/login with valid user data.

- Perform a request to retrieve the user ID GET/users.

- Perform a request to create an animal POST/pet with valid data.

- Perform the image upload method POST/pet/{id}/image.

- Perform a request to get information about the created animal GET/pet/{id}.

- Perform a request to update the animal's information PATCH/pet with valid new data.

- Perform a request to add a like to the animal PUT/pet/{id}/like.

- Perform a request to delete the animal DELETE/pet/{id}.

Expected Results:

- User is deleted successfully.
- Token is received.
- User ID is retrieved.
- Animal ID is retrieved.
- Image is successfully uploaded, and a link is returned.
- Animal information is retrieved.
- Animal information is updated, and the animal ID is received.
- Like is added.
- Animal is deleted.
