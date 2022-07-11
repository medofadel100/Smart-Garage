from firebase import firebase
firebase = firebase.FirebaseApplication('https://smart-garage-bbe06-default-rtdb.firebaseio.com/', None)
result = firebase.get('Compound%20Gate%20QR%20', None)
print (result)