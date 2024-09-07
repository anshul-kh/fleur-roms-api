from api.operations.steps import get_steps
from api.operations.roms import new_rom_record,get_all_roms,add_new_build,get_rom,get_rom_by_id
from flask import request,Blueprint,jsonify

roms = Blueprint('roms',__name__)

@roms.route('/', methods=['GET'])
def root():
    return "Server Up and Running"

@roms.route('/steps',methods=['GET'])
def steps():
    res = get_steps()
    return jsonify(res)

@roms.route('/roms',methods=['GET'])
async def list_roms():
    res = await get_all_roms()
    return res
    
@roms.route('/search/<name>',methods=['GET'])
async def search_rom(name):
    try:
        name = str(name)
        res = await get_rom(name)
        return res
    except Exception as e:
        return jsonify({'err':str(e)}),500
        
@roms.route('/rom/<id>',methods=['GET'])
async def search_rom_by_id(id):
    try:
        rom_id = int(id)
        res = await get_rom_by_id(rom_id)
        return res
    except Exception as e:
        return jsonify({'err':str(e)}),500
        
 
@roms.route('/rom',methods=['POST'])
async def do_entry():
    try:
        data = request.get_json()
        if data is None or len(data) == 0:
            return jsonify({'err':'Invalid/Empty Data Format','suggestion':'Use JSON Format in Body'}),400
        res = await new_rom_record(data)
        return res 
    except Exception as e:
        return jsonify({'err':str(e)}),500
        

@roms.route('/build',methods=['POST'])
async def add_build():
    try:
        data =  request.get_json()
        if data is None or len(data) == 0:
            return jsonify({'err':'Invalid/Empty Data Format','suggestion':'Use JSON Format in Body'}),400
        
        res = await add_new_build(data)
        return res
    except Exception as e:
        return jsonify({'err':str(e)}),500 
        