from flask import Flask,request

app = Flask(__name__)

# create the idea repository
ideas={
    1 :{
        "id" : 1,
        "idea_name" : "Save soil",
        "idea_description" :"Details about Saving Soil",
        "idea_author" :"kusum"
    },
    
    2 :{
        "id" : 2,
        "idea_name" : "ONDC",
        "idea_description" :"DETAIL ONDC",
        "idea_author" :"SUNIL"    
        
    }
    # type: ignore
}
'''Create an RESTful endpoint for feteching the ideas'''
@app.get("/ideaapp/appi/v1/ideas")

def get_all_ideas():
    # I need to raed the query param
    idea_author =request.args.get('idea_author')
    
    if idea_author:
        #filter the idea created by this author
        idea_res={}
        for key,value in ideas.items():
            if value["idea_author"]==idea_author:
                idea_res[key] =value
        return idea_res        
        
    # logic to fetch all the ideas and support query params
    return ideas




'''create a restfull endpoint for creating a new idea'''
@app.post("/ideaapp/appi/v1/ideas")
def create_idea():
    #logic to create a new idea
    try:
        #first read the request body
        request_body=request.get_json()
        print(request_body)
        #check if the idea  id passed is not present already
        if request_body["id"] in ideas:
            return "idea with the name same id already present",400
        # insert the passed idea in the ideas dictionary
        ideas[request_body["id"]] = request_body
        # return the response saying idea got saved
        return "idea created and saved sucessfully ",201
    except KeyError:
        return "id is missing",400
    except :
        return  "some internal server error",500
    
    
'''
End point to fetech idea based on the idea id
'''
@app.get("/ideaapp/appi/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
    except:
        return"some internal error happened",500
'''
Endpoint for updating the idea
'''
@app.put("/ideaapp/appi/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json() #request body and updating the dictionary
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
    except:
        return"some internal error happened",500
'''
End point to delete an idea 
'''
@app.put("/ideaapp/appi/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id)) #delete the entery from the dictionary
            return"idea got suceefully removed"
        else:
            return "idea id passed is not present",400
    except:
        return"some internal error happened",500


if __name__ == '_main_':
    app.run(port=8080)