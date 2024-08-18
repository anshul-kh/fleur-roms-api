from flask import Blueprint,request,jsonify
from api.operations.recovery import new_recov_record,get_all_recovery

recovery = Blueprint('recov',__name__)

@recovery.route('/recovery',methods=['GET','POST'])
async def recov():
    # GET Request
    if  request.method == 'GET':
        res = await get_all_recovery()

        if res is None:
            return jsonify({'err':'No Records Found'}),404
        
        return res,200
        
    #POST Request 
    elif request.method == 'POST':
     data = request.get_json()
     
     if data is None or len(data) == 0:
         return jsonify({'err':'Invalid/Empty Data Format','suggestion':'Use JSON Format in Body'}),400
    
     name =   data.get('name')
     version  = data.get('version')
     modified = data.get('modified')
     tested =  data.get('tested')
     download = data.get('download')
     
     res = await new_recov_record(name,version,modified,tested,download)
     
     if res is None:
         return jsonify({'err':'An error occurred while creating record'}),500
    
     return jsonify({'msg':'Record Created Successfully'}),201
   