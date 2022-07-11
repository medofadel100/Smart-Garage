from firebase import firebase
firebase = firebase.FirebaseApplication('https://login-egy-park-default-rtdb.firebaseio.com/', None)

result = firebase.get('/user','')
print (result)