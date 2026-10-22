import requests
new_comment={
    "name":"john done",
    "email":"john1213@gmail.com",
    "body":"tihs is a new comment",
    "postId":1
}


response= requests.get("https://jsonplaceholder.typicode.com/comments")

if response.status_code==200:
    data=response.json()
    print(data)
    print("sucess data retrieved.")
else:
    print(f"Error:{response.status_code}")