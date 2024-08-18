from . import db
from prisma.models import Recovery
from datetime import datetime
from flask import jsonify

# Create a new recovery record
async def new_recov_record(name, version, modified, tested, download):
    try:
        await db.connect()

        if isinstance(modified, str):
            modified = datetime.fromisoformat(modified)
        elif isinstance(modified, datetime):
            pass 
        else:
            raise ValueError("Invalid modified date format")

        entry = await Recovery.prisma().create(
            data={
                'name': name,
                'version': version,
                'modified': modified,
                'tested': tested,
                'download': download,
            },
        )
        return entry
        
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})
    finally:
        await db.disconnect()


# Fetch the recovery records
async def get_all_recovery():
    try:
        await db.connect()
        res = await Recovery.prisma().find_many()

        res_dict = [
            {
                'id': item.id,
                'name': item.name,
                'version': item.version,
                'modified': item.modified.isoformat() if item.modified else None,
                'tested': item.tested,
                'link': item.download
            }
            for item in res
        ]

        return jsonify({'data': res_dict, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})
    finally:
        await db.disconnect()