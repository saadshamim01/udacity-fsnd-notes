#Getting user data from View

Reference Link: https://classroom.udacity.com/nanodegrees/nd0044/parts/216c669c-5e62-43a1-bcb9-8a8e5eca972a/modules/3d18d16d-51ba-48ac-9916-e770981c3f7e/lessons/31c3741e-ea1c-48d5-a9bd-2d1d0bb33e5d/concepts/5424e14d-2fa8-41b8-83b7-8aece3b5359e

- 3 methods

For URL query parameters: /foo?field1-value1 use request.args
value1 = request.args.get('field1')

For form inputs, use request.form
username = request.form.get('username')
password = request.form.get('password')


For data type application/json, use request dat
data_string = request.data
data_dictionary = json.loads(data_string)
