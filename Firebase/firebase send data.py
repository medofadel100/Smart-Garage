from firebase import firebase
firebase = firebase.FirebaseApplication('https://login-egy-park-default-rtdb.firebaseio.com/', None)
data = {
    'name': 'Ahmed',
    'email': 'medofadel100@gmail.com',
    'phone': '01223840100',
    'password': '11A22B33C'
}
result = firebase.post('/user',data)
print (result)