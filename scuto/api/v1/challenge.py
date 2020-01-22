from scuto.models import Challenge, Flag
from scuto.docker import search_image
from scuto.util.decorators import jsonify
from .router import routes


load = 0

@routes('/challenge/search')
@jsonify()
async def search(request):
    term, page, page_size = request.query.get('q'), request.query.get('page'), request.query.get('page_size')
    return await search_image(term, page, page_size)

@routes('/challenge/list')
@jsonify()
async def list_challenges(request):
    return Challenge.objects()

@routes('/challenge/edit_challenge', methods=['POST'])
@jsonify()
async def edit_challenge(request):
    challenge = Challenge.from_json(await request.json())
    challenge.save()
    return {
        'status': 'success'
    }