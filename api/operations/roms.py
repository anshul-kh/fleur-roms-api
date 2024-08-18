from prisma import Client, register
from . import db
from flask import jsonify
from prisma.models import Roms,Builds
from datetime import datetime

async def new_rom_record(props):    
    try:
        await db.connect()
        modified = props.get('build').get('modified')
        
        if isinstance(modified, str):
            modified = datetime.fromisoformat(modified)
        elif isinstance(modified, datetime):
            pass 
        else:
            raise ValueError("Invalid modified date format")
            
        entry = await Roms.prisma().create(
            data={
                'name': props.get('name').lower(),
                'discription': props.get('description'),
                'tested' : props.get('tested'),
                'android_version' : props.get('android_version'),
                'build' : {
                    'create': {
                        'tested': props.get('build').get('tested'),
                        'download': props.get('build').get('download'),
                        'modified': modified  
                    }
                }
            },
        )
        if entry is None:
            return jsonify({'err':'An error occurred while creating record'}),500
       
        return jsonify({'msg':'Record Created Successfully'}),201
        
    except Exception as e:
        return {'err':str(e),'suggesstion': 'Check Out Docs Properly'}
    finally:
        await db.disconnect()



# Fetch all the roms
async def get_all_roms():
    try:
        await db.connect()
        res = await Roms.prisma().find_many(
            include={
                'build': True  
            }
        )

        res_dict = [
            {
                'id': item.id,
                'name': item.name,
                'discription': item.discription,
                'tested': item.tested,
                'android_version': item.android_version,
                'build': [
                    {
                        'id': build.id,
                        'rom_id': build.rom_id,
                        'modified': build.modified.isoformat() if build.modified else None,
                        'tested': build.tested,
                        'download': build.download
                    }
                    for build in item.build
                ] if item.build else []
            }
            for item in res
        ]

        return jsonify({'data': res_dict, 'success': True})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e), 'success': False})
    finally:
        await db.disconnect()



# Add new Build for existing ROM
async def add_new_build(props):
    try:
        await db.connect()
        rom = await Roms.prisma().find_unique(where={'id':props.get('rom_id')})
        if rom is None:
            return jsonify({'err':'No Rom Found with this ID'}),404
        
        modified = props.get('modified')
        if isinstance(modified, str):
            modified = datetime.fromisoformat(modified)
        elif isinstance(modified, datetime):
            pass 
        else:
            raise ValueError("Invalid modified date format")       
        
        new_build = await Builds.prisma().create(
            data={
                'modified':modified,
                'tested':props.get('tested'),
                'download':props.get('download'),
                'rom':{
                    'connect':{
                        'id':props.get('rom_id')
                    }
                }
            }
        )
        
        if new_build is None:
            return jsonify({'err':'An error occurred while creating record'}),500
        
        return jsonify({'msg':'Record Created Successfully'}),201
    except Exception as e:
        return {'err':str(e),'suggesstion': 'Check Out Docs Properly'}
    finally:
        await db.disconnect()    
        

async def get_rom(name):
    try:
        await db.connect()
        rom = await Roms.prisma().find_many(
            where={'name':name},
            include={
                'build': True  
            }
        )
        
        if rom is None:
            return jsonify({'err':'No Rom Found with this Name'}),404
        
        res_dict = [
            {
                'id': item.id,
                'name': item.name,
                'discription': item.discription,
                'tested': item.tested,
                'android_version': item.android_version,
                'build': [
                    {
                        'id': build.id,
                        'rom_id': build.rom_id,
                        'modified': build.modified.isoformat() if build.modified else None,
                        'tested': build.tested,
                        'download': build.download
                    }
                    for build in item.build
                ] if item.build else []
            }
            for item in rom
        ]
        
        return jsonify({'data': res_dict, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})
    finally:
        await db.disconnect()